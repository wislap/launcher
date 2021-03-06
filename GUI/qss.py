button_qss_1 = '''
           QPushButton {    

    /* 边框风格 */  
    border-style:outset;  

    /* 边框宽度 */  
    border-width:2px;  

    /* 边框颜色 */  
    border-color:rgb(10,45,110);  

    /* 边框倒角 */  
    border-radius:10px;  

    /* 字体 */  
    font:bold 14px;  

    /* 控件最小宽度 */  
    min-width:100px;  

    /* 控件最小高度 */  
    min-height:20px;  

    /* 内边距 */  
    padding:4px;  
}  

/* 鼠标按下时的效果 */  
QPushButton#pushButton:pressed {  
    /* 改变背景色 */  
    background-color:rgb(40,85,20);  

    /* 改变边框风格 */  
    border-style:inset;  

    /* 使文字有一点移动 */  
    padding-left:6px;  
    padding-top:6px;  
}  

/* 按钮样式 */  
QPushButton:flat {  
    border:2px solid red;  
}  
           '''