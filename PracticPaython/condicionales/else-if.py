ingreso_mensual = 81000
gasto_mensual = 80000

#if anidados else y if (elif)

if ingreso_mensual >10000:
    if ingreso_mensual - gasto_mensual < 0:
     print("estas bien economicamente")
    elif ingreso_mensual - gasto_mensual >3000:
        print("bien, estas bien")
    else:
        print("estas gastando una banda, hay que mirar si te alcanza")

elif ingreso_mensual >100000:
    print("estas bien en cualquier parte")# segunda condicion(puede colocar varios elif)

elif ingreso_mensual >200:
     print("sos ppbre")    