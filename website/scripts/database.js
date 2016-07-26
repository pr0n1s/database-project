// Sends the received value server-side to query.php
function query(str){
  if(str == ""){
    document.getElementById("query").innerHTML = "";
    return;
  }else{
    if(window.XMLHttpRequest){
      xmlhttp = new XMLHttpRequest();
    }else{
      xmlhttp = new ActiveXObject("Microsoft.XMLHTTP");
    }
    xmlhttp.onreadystatechange = function(){
      if(xmlhttp.readyState == 4 && xmlhttp.status == 200){
        document.getElementById("query").innerHTML = xmlhttp.responseText;
      }
    };
    xmlhttp.open("GET", "query.php?q="+str, true);
    xmlhttp.send();
  }
}
