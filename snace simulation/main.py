from turtle import pos
from GRPgraph import py2D

win = py2D.Screen_([900,700])


m = py2D.Math_()
mouse = py2D.Sub_.Mouse()


dot2_col = py2D.Color_(0,200,0) ; dot2 = win.Shape2D.Rect(dot2_col.color,[500,500],[10,10],0,win.screen)


poses = [[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]]
x=0 ; y=0

def App():
    global x,y,poses

    
    dot2.Set_pos(mouse.Get_Pos())
    doting = win.Shape2D.Rect('blue',[x,y],[10,10],0,win.screen)
    
    spedx = (dot2.pos[0]-doting.pos[0])/14
    spedy = (dot2.pos[1]-doting.pos[1])/14
    x+=spedx
    y+=spedy

    for i in range(len(poses)):
        if i==0:
            spedxs = (doting.pos[0]-poses[i][0])/14
            spedys = (doting.pos[1]-poses[i][1])/14
            poses[i][0]+=spedxs
            poses[i][1]+=spedys

            line1 = win.Shape2D.Line((int(255/(i+1)),0,0),poses[i],[x,y],15,win.screen).Draw()
        else:
            spedys = (poses[i-1][1]-poses[i][1])/14
            spedxs = (poses[i-1][0]-poses[i][0])/14
            poses[i][0]+=spedxs
            poses[i][1]+=spedys
            
            line1 = win.Shape2D.Line((int(255-60/i),0,0),poses[i],poses[i-1],int(15/i),win.screen).Draw()
    
    
    

    line1 = win.Shape2D.Line((255,0,0),[x,y],dot2.pos,15,win.screen).Draw()





while win.close():
    win.Update().BG_col('black')
    win.set_fps(60)
    App()

    