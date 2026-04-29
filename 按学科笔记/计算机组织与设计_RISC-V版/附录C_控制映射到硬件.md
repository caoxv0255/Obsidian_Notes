# 附录C 控制映射到硬件

> **附录目标**：深入理解控制单元的设计原理，掌握有限状态机和微程序设计

---

## 📖 附录概述

本附录介绍控制单元的设计方法，包括：

- 组合控制单元
- 有限状态机控制
- 微程序设计

通过本附录学习，你将理解如何将控制逻辑映射到硬件。

---

## 📚 核心内容

### C.1 引言

#### 控制单元的作用

**定义**：产生控制信号，指挥数据通路

**作用**：
- 指令译码
- 产生控制信号
- 控制数据流

---

### C.2 实现组合控制单元

#### 组合控制单元

**定义**：输出仅取决于当前输入

**设计方法**：
1. 确定控制信号
2. 确定输入信号
3. 设计逻辑电路

#### 示例

**ALU控制**：
```
输入：ALUOp, funct3, funct7
输出：ALU控制信号
```

**逻辑**：
```verilog
module alu_control(
    input [1:0] alu_op,
    input [2:0] funct3,
    input [6:0] funct7,
    output reg [3:0] alu_control
);
    always @(*) begin
        case (alu_op)
            2'b00: alu_control = 4'b0010;  // add
            2'b01: alu_control = 4'b0110;  // sub
            2'b10: begin
                case (funct3)
                    3'b000: alu_control = 4'b0010;  // add
                    3'b010: alu_control = 4'b0000;  // and
                    3'b011: alu_control = 4'b0001;  // or
                    3'b111: alu_control = 4'b0111;  // andn
                    default: alu_control = 4'b0000;
                endcase
            end
            default: alu_control = 4'b0000;
        endcase
    end
endmodule
```

---

### C.3 实现有限状态机控制

#### 有限状态机(FSM)

**定义**：具有有限状态的系统

**类型**：
- Moore型：输出仅取决于状态
- Mealy型：输出取决于状态和输入

#### FSM设计步骤

1. **确定状态**：识别系统状态
2. **确定状态转换**：定义状态间的转换条件
3. **确定输出**：定义每个状态的输出
4. **实现状态机**：使用硬件或软件实现

#### 示例：多周期处理器FSM

**状态**：
- Fetch
- Decode
- Execute
- Memory
- Writeback

**状态转换**：
```
Fetch → Decode → Execute → Memory → Writeback
```

**Verilog实现**：
```verilog
module controller_fsm(
    input clk,
    input rst,
    input [6:0] opcode,
    output reg [1:0] pc_source,
    output reg mem_read,
    output reg mem_write,
    output reg reg_write
);
    reg [2:0] state, next_state;

    parameter FETCH   = 3'b000;
    parameter DECODE  = 3'b001;
    parameter EXECUTE = 3'b010;
    parameter MEMORY  = 3'b011;
    parameter WB      = 3'b100;

    always @(posedge clk or posedge rst) begin
        if (rst)
            state <= FETCH;
        else
            state <= next_state;
    end

    always @(*) begin
        next_state = FETCH;
        case (state)
            FETCH: next_state = DECODE;
            DECODE: next_state = EXECUTE;
            EXECUTE: begin
                case (opcode)
                    7'b0000011: next_state = MEMORY;  // load
                    7'b0100011: next_state = MEMORY;  // store
                    7'b0110011: next_state = WB;      // R-type
                    default: next_state = FETCH;
                endcase
            end
            MEMORY: next_state = WB;
            WB: next_state = FETCH;
            default: next_state = FETCH;
        endcase
    end

    always @(*) begin
        pc_source = 2'b00;
        mem_read = 0;
        mem_write = 0;
        reg_write = 0;

        case (state)
            FETCH: begin
                mem_read = 1;
            end
            MEMORY: begin
                case (opcode)
                    7'b0000011: mem_read = 1;  // load
                    7'b0100011: mem_write = 1; // store
                endcase
            end
            WB: begin
                reg_write = 1;
            end
        endcase
    end
endmodule
```

---

### C.4 使用定序器实现下一状态函数

#### 定序器

**定义**：控制状态转换的电路

**作用**：
- 确定下一个状态
- 处理条件跳转

#### 实现方法

**1. 硬连线**：
- 固定状态转换
- 简单但灵活

**2. 微程序**：
- 使用微指令控制
- 灵活但复杂

---

### C.5 将微程序转换为硬件

#### 微程序

**定义**：使用微指令控制硬件

**组成**：
- 微指令存储器
- 微指令寄存器
- 微地址生成

#### 微指令格式

**水平微指令**：
- 每位对应一个控制信号
- 宽但灵活

**垂直微指令**：
- 编码的控制信号
- 窄但需要译码

#### 示例

**微指令**：
```
控制信号：PCWrite, IorD, MemRead, MemWrite, IRWrite, ...
```

**微程序**：
```
FETCH:  PCWrite=0, IorD=0, MemRead=1, MemWrite=0, IRWrite=1, ...
DECODE: PCWrite=0, IorD=0, MemRead=0, MemWrite=0, IRWrite=0, ...
```

---

### C.6 总结

#### 附录要点

1. **组合控制单元**：输出仅取决于输入
2. **有限状态机**：状态转换系统
3. **微程序**：使用微指令控制硬件
4. **控制单元设计**：选择合适的方法

#### 学习建议

1. **理解原理**：深入理解控制单元原理
2. **动手实践**：设计简单的控制单元
3. **仿真验证**：使用仿真工具验证设计
4. **综合实现**：将设计综合到硬件

---

**附录C结束** → 附录D：[[附录D_指令集架构概述]]