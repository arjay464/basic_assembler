@0//register to be set to -1
M=0
@1 //horizontal shift of the box
M=0
@2 //vertical shift of the box
M=0
@3 //polarity of the box-row (1 = indented)
M=0
@4 //progress of each box
M=0
@5 //vertical shift of each row
M=0
@6 //progress of each row
M=0
@7 //board progress
M=0


(CHK)//draw a checkboard
@1
M=0
@16
D=A
@7
D=D-M
@END
D;JEQ

(ROW) //create a row with veritcal shift @5 and polarity @3
@5
D=M
@2
M=D
@3
D=M
@IND 
D-1;JEQ //@3 = 1, row should be indented
@BOX
0;JMP

(IND)
@1
M=1

(ROWLOOP)
@16
D=A
@6
D=D-M
@CHKN //set dest to new row selection
D;JEQ

(BOX) //create a box with top corner @1,@2
@16384
D=A
@0
M=D
@1
D=M
@0
M=M+D //add horizontal shift
@2
D=M
@0
M=M+D //add vertical shift

(LOOP)
@16
D=A
@4
D=D-M
@ROWN //set jump dest to row shft
D;JEQ

@0
A=M //set current address to register
M=-1
@32
D=A
@0
M=M+D //set next register to the one directly under this one
@4
M=M+1 //increment
@LOOP
0;JMP


(ROWN)
@2
D=A
@1
M=M+D
@6
M=M+1
@4
M=0
@ROWLOOP
0;JMP


(CHKN)
@512
D=A
@5
M=M+D
@7
M=M+1
@3
D=M
@6
M=0
@SFT
D-1;JEQ

@3
M=1
@CHK
0;JMP

(SFT)
@3
M=0
@CHK
0;JMP

(END)
@END
0;JMP


