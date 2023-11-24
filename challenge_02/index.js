`"#" Incrementa el valor numérico en 1.
"@" Decrementa el valor numérico en 1.
"*" Multiplica el valor numérico por sí mismo.
"&" Imprime el valor numérico actual.
`

const message = "&###@&*&###@@##@##&######@@#####@#@#@#@##@@@@@@@@@@@@@@@*&&@@@@@@@@@####@@@@@@@@@#########&#&##@@##@@##@@##@@##@@##@@##@@##@@##@@##@@##@@##@@##@@##@@##@@&"
let init_val = 0
let sol = ""
for(var i=0; i<message.length; i++){
  if(message[i] == "#"){
    init_val+=1;
  }else if(message[i] == "@"){
    init_val-=1;
  }else if(message[i] == "*"){
    init_val = init_val * init_val
  } else {
    sol+= String(init_val)
  }
}

document.getElementById("response").innerHTML = sol