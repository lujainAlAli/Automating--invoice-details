
function add_loc(evt){
    if (evt.target.value==="other"){
        var loc=document.getElementById("locations");
        var option= document.createElement("option");
        option.text= prompt("enter new location:")
        loc.add(option);
    }
}