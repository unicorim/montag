WebRequest := Object clone do(
    handleSocket := method(aSocket,
        aSocket streamReadNextChunk
        request := aSocket readBuffer \
		   betweenSeq("GET ", " HTTP")
        f := File with(request) 
        if(f exists, 
	     	     f streamTo(aSocket)
		       , 
				aSocket streamWrite("not found")
					)
        aSocket close
    )
)

WebServer := Server clone do(
    setPort(8000)
    handleSocket := method(aSocket, 
        WebRequest clone asyncSend(handleSocket(aSocket))
    )
)

WebServer start