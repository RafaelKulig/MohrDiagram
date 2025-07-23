import math
def main():
    while True:
        print("Insert \u03C3x, \u03C3y and \u03C4xy separeted by space: ", end="")
        stress=input().split(" ")
        try:
            s_x=float(stress[0])
            s_y=float(stress[1])
            t_xy=float(stress[2])
            break
        except:
            print("Please, include only float type.",end='\n')
    maindata=calculate(s_x,s_y,t_xy)
    print(f"Average normal stress: {maindata[0]:.2f}\nMaximum shear: {maindata[1]:.2f}\nPrincipal stress:\n\t1:{maindata[2]:.2f}\n\t2:{maindata[3]:.2f}\nMain plane: {maindata[4]/2:.2f}")
        

def calculate(s_x:float,s_y:float,t_xy:float):
    avg_stress=(s_x+s_y)/2
    radius=pow(pow((s_x-s_y)/2,2)+t_xy**2,0.5)
    stress1=avg_stress+radius
    stress2=avg_stress-radius
    theta_2=rad2deg(math.atan(2*t_xy/(s_x-s_y)))
    return(avg_stress,radius,stress1,stress2,theta_2)


def rad2deg(angle):
    return angle*180/math.pi
if __name__=="__main__":
    main()