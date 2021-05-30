from myhdl import block, Signal, instances, always, intbv, bin
import math


@block
def dmem(clk, addr, din, be, wren):
    dout = Signal(intbv(0, min=-(math.pow(2, 31)), max=(math.pow(2, 31) - 1)))

    dmem = [intbv(0, min=-(math.pow(2, 31)), max=(math.pow(2, 31) - 1)) for i in range(1024)]

    @always(clk.posedge)
    def seq():
        if wren:
            if bin(be) == '1111':
                dmem[addr] = din
            elif bin(be) == '1100':
                dmem[addr][31:16] = din[15:0]
            elif bin(be) == '0011':
                dmem[addr][15:0] = din[15:0]
            elif bin(be) == '1000':
                dmem[addr][31:24] = din[7:0]
            elif bin(be) == '0100':
                dmem[addr][23:16] = din[7:0]
            elif bin(be) == '0010':
                dmem[addr][15:8] = din[7:0]
            elif bin(be) == '0001':
                dmem[addr][7:0] = din[7:0]

        dout.next = dmem[addr]

    return instances()