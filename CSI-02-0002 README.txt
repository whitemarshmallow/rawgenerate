Channel configurations:
Scenario:	Dense Urban (Macro only)
Frequency Range:	FR1 only,  2GHz 
Inter-BS distance:	200m
Channel model:	According to TR 38.901
Antenna setup and port layouts at gNB:	32 ports: (8,8,2,1,1,2,8), (dH,dV) = (0.5, 0.8)
Antenna setup and port layouts at UE:	4RX: (1,2,2,1,1,1,2), (dH,dV) = (0.5, 0.5)
Bandwidth:    10M(52RB),
SCS:   15kHz for 2GHz

Dataset configurations:
Data type:  channel in Frequency domain each sample includes 20 TTI in Time domain and 8 RBs in Frequency domain, The TTI interval is 5 ms
Data size:   (21000,20,2 , 32, 4, 8)  ---> (UE number, Time,Real&Imaginary parts, Tx, Rx,RB number)