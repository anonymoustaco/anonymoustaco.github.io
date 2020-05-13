       function psw() {
            var x = document.getElementById("myPsw").value;
            var y = ("test")
            var z = ("error")
            document.getElementById("myPsw")
            if (x != "4PCRR") {
                alert("error")
                document.getElementById("demo").innerHTML = z
            }
            if (x == "4PCRR" ) {
                document.getElementById("demo").innerHTML = y;
            }
            
        }
