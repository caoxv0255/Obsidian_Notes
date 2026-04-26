# API接口与封装

## 核心概念

API（Application Programming Interface）是量化交易系统与券商/交易所通信的桥梁。不同券商提供不同类型的接口——FIX协议、RESTful API、WebSocket流数据等，理解这些接口的特性与适用场景是构建实盘系统的必备基础。

券商API的核心功能包括：**行情订阅**（获取实时价格、成交量）、**订单发送**（市价单、限价单、条件单）、**持仓查询**（当前仓位、盈亏情况）、**账户信息**（资金余额、保证金要求）。一个设计良好的API封装层需要屏蔽不同券商接口的差异，提供统一的上层接口，使策略代码不依赖于具体券商实现。

对于申请顶尖量化金融项目的学生来说，理解API接口的设计哲学——包括错误处理、重试机制、超时管理——不仅对交易系统开发有用，更是软件工程能力的直接体现。

## 方法论

### 主流券商接口类型

| 接口类型 | 代表券商/平台 | 延迟 | 适用场景 |
|---------|-------------|------|---------|
| FIX 4.2/4.4 | 机构级（Citadel, Two Sigma） | 微秒级 | 高频交易 |
| REST API | Interactive Brokers, Alpaca | 毫秒级 | 中频策略 |
| WebSocket | Binance, Bybit, 聚宽 | 毫秒级 | 数字货币/零售 |
| SDK（Python/Java） | 聚宽、米筐、掘金 | 毫秒级 | 快速开发 |

### API封装设计原则

1. **接口一致性**：不同券商的API命名、参数格式差异巨大，封装层需要提供统一接口。例如，无论哪家券商，发送市价单的函数都应该是 `send_market_order(symbol, quantity)`。

2. **错误处理**：网络抖动、券商服务宕机、订单被拒绝等情况需要完善的异常处理机制。建议使用**指数退避（Exponential Backoff）**进行重试，并设置最大重试次数防止无限循环。

3. **连接管理**：长连接（WebSocket/FIX）需要心跳机制检测存活，断线后自动重连；短连接（REST）需要注意并发限制与速率限制。

4. **类型安全**：使用强类型语言（C++/Java）可以获得编译期检查，Python可使用`dataclass`或`pydantic`提供运行时类型验证。

## 代码实现

以下是一个券商API统一封装的设计示例（Python）：

```python
import asyncio
import time
from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from enum import Enum
from typing import Dict, List, Optional
import logging
from decimal import Decimal

logger = logging.getLogger(__name__)

class OrderSide(Enum):
    BUY = "BUY"
    SELL = "SELL"

class OrderType(Enum):
    MARKET = "MARKET"
    LIMIT = "LIMIT"
    STOP = "STOP"
    STOP_LIMIT = "STOP_LIMIT"

class OrderStatus(Enum):
    PENDING = "PENDING"
    SUBMITTED = "SUBMITTED"
    PARTIAL_FILLED = "PARTIAL_FILLED"
    FILLED = "FILLED"
    CANCELLED = "CANCELLED"
    REJECTED = "REJECTED"

class TimeInForce(Enum):
    DAY = "DAY"
    GTC = "GTC"
    IOC = "IOC"
    FOK = "FOK"

@dataclass
class Order:
    order_id: str
    symbol: str
    side: OrderSide
    order_type: OrderType
    quantity: Decimal
    price: Optional[Decimal] = None
    stop_price: Optional[Decimal] = None
    tif: TimeInForce = TimeInForce.DAY
    status: OrderStatus = OrderStatus.PENDING
    filled_qty: Decimal = field(default_factory=lambda: Decimal('0'))
    avg_fill_price: Optional[Decimal] = None
    created_at: float = field(default_factory=time.time)
    updated_at: float = field(default_factory=time.time)

@dataclass
class Position:
    symbol: str
    quantity: Decimal
    avg_cost: Decimal
    unrealized_pnl: Decimal

@dataclass
class Account:
    account_id: str
    cash: Decimal
    equity: Decimal
    buying_power: Decimal

class BrokerBase(ABC):
    @abstractmethod
    async def connect(self) -> bool: pass
    
    @abstractmethod
    async def disconnect(self): pass
    
    @abstractmethod
    async def send_order(self, order: Order) -> Order: pass
    
    @abstractmethod
    async def cancel_order(self, order_id: str) -> bool: pass
    
    @abstractmethod
    async def get_positions(self) -> List[Position]: pass
    
    @abstractmethod
    async def get_account(self) -> Account: pass

class IBKRBroker(BrokerBase):
    def __init__(self, host: str = "127.0.0.1", port: int = 7497, client_id: int = 1):
        self.host = host
        self.port = port
        self.client_id = client_id
        self._connected = False
        self._orders: Dict[str, Order] = {}
    
    async def connect(self) -> bool:
        try:
            self._connected = True
            logger.info(f"Connected to IBKR at {self.host}:{self.port}")
            return True
        except Exception as e:
            logger.error(f"Failed to connect: {e}")
            return False
    
    async def disconnect(self):
        self._connected = False
        logger.info("Disconnected from IBKR")
    
    async def send_order(self, order: Order) -> Order:
        if not self._connected:
            raise ConnectionError("Not connected to broker")
        
        order.order_id = f"ORD_{int(time.time() * 1000)}"
        order.status = OrderStatus.SUBMITTED
        self._orders[order.order_id] = order
        logger.info(f"Order submitted: {order.order_id}")
        asyncio.create_task(self._simulate_fill(order))
        return order
    
    async def _simulate_fill(self, order: Order, delay: float = 0.1):
        await asyncio.sleep(delay)
        order.status = OrderStatus.FILLED
        order.filled_qty = order.quantity
        order.avg_fill_price = order.price or Decimal('100.0')
        logger.info(f"Order filled: {order.order_id}")
    
    async def cancel_order(self, order_id: str) -> bool:
        if order_id in self._orders:
            self._orders[order_id].status = OrderStatus.CANCELLED
            return True
        return False
    
    async def get_positions(self) -> List[Position]:
        return []
    
    async def get_account(self) -> Account:
        return Account("DU123456", Decimal('100000'), Decimal('100000'), Decimal('400000'))

class RetryHandler:
    """带重试机制的API调用封装"""
    
    def __init__(self, max_retries: int = 3, base_delay: float = 1.0):
        self.max_retries = max_retries
        self.base_delay = base_delay
    
    async def execute_with_retry(self, func, *args, **kwargs):
        last_exception = None
        for attempt in range(self.max_retries):
            try:
                return await func(*args, **kwargs)
            except Exception as e:
                last_exception = e
                delay = self.base_delay * (2 ** attempt)
                logger.warning(f"Attempt {attempt+1} failed: {e}. Retrying in {delay}s...")
                await asyncio.sleep(delay)
        raise last_exception
```

## 应用与局限

### 实际应用

1. **多券商切换**：统一API封装使得策略可以在不同券商间切换，只需替换Broker实现而无需修改策略代码。

2. **模拟交易测试**：使用Mock Broker可以在不消耗真实资金的情况下完整测试交易逻辑。

3. **策略监控**：通过统一的API层可以方便地添加日志、监控和报警功能。

### 局限性

1. **协议差异**：某些券商特有的功能（如篮子订单、挂钩条件单）难以用统一接口完全覆盖。

2. **性能开销**：抽象层会带来一定的性能损失，对于延迟敏感的高频策略可能需要直接使用原生API。

3. **错误恢复复杂性**：不同券商的错误码体系不同，封装层需要维护详尽的错误映射表。

---

**延伸阅读**：
- Interactive Brokers API Documentation
- FIX Protocol 4.4 Specification (FIX Trading Community)
