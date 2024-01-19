function showNum(val){
    document.getElementById('res').value+=val;
}
function result(){
    var v1 = document.getElementById('res').value;
    var v2 = eval(v1);
    document.getElementById('res').value = v2;
}
function Clear(){
    document.getElementById('res').value='';
}
function back(){
    var v = document.getElementById('res');
    v.value=v.value.slice(0,-1);
    
}