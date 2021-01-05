import vrep
from pedrohj import *

# Configurations (Setup)

robo = objeto()
motor1 = robo.obter("DynamicLeftJoint")
motor2 = robo.obter("DynamicRightJoint")
#End here

#Infinty loop
while True: 
    robo.velocidade(motor1, 20) #go forward
    robo.velocidade(motor2, 20)
    robo.delay(1000) #wait 1000 ms = 1s
    robo.velocidade(motor1, 20)
    robo.velocidade(motor2, 0)
    robo.delay(3000) 