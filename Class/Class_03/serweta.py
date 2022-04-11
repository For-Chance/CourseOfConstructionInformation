def serweta(zolw):

    def kwadrat(zolw, dlug):
        for i in range(4):
            zolw.fd(dlug)
            zolw.left(90)

    for i in range(36):
        kwadrat(zolw, 100)
        zolw.left(10)