
const form = document.querySelector("form");

if(form){

form.addEventListener("submit",function(){

const btn = document.querySelector("button");

btn.innerHTML="⏳ Generating...";

btn.disabled=true;

});

}
