// ==========================================
// AI Product Description Generator
// script.js
// ==========================================

const generateBtn = document.getElementById("generateBtn");

const loader = document.getElementById("loader");

const productImage = document.getElementById("productImage");


// ------------------------------
// Category Images
// ------------------------------

const images = {

    Electronics:"https://cdn-icons-png.flaticon.com/512/3659/3659899.png",

    Mobile:"https://cdn-icons-png.flaticon.com/512/545/545245.png",

    Laptop:"https://cdn-icons-png.flaticon.com/512/679/679720.png",

    Watch:"https://cdn-icons-png.flaticon.com/512/2920/2920329.png",

    Shoes:"https://cdn-icons-png.flaticon.com/512/2589/2589903.png",

    Fashion:"https://cdn-icons-png.flaticon.com/512/892/892458.png",

    Beauty:"https://cdn-icons-png.flaticon.com/512/3163/3163203.png",

    "Home Appliance":"https://cdn-icons-png.flaticon.com/512/1046/1046857.png",

    Kitchen:"https://cdn-icons-png.flaticon.com/512/3075/3075977.png",

    Furniture:"https://cdn-icons-png.flaticon.com/512/809/809957.png",

    Sports:"https://cdn-icons-png.flaticon.com/512/857/857455.png"

};


// ------------------------------
// Change Image
// ------------------------------

document
.getElementById("category")
.addEventListener("change",function(){

productImage.src = images[this.value];

});


// ------------------------------
// Generate AI
// ------------------------------

generateBtn.onclick = async ()=>{

const product_name=document.getElementById("product_name").value;

const brand=document.getElementById("brand").value;

const price=document.getElementById("price").value;

const category=document.getElementById("category").value;

const features=document.getElementById("features").value;

const tone=document.getElementById("tone").value;

const audience=document.getElementById("audience").value;

const language=document.getElementById("language").value;


// Validation

if(product_name==""){

alert("Enter Product Name");

return;

}

if(features==""){

alert("Enter Product Features");

return;

}

loader.style.display="flex";

document.getElementById("output").style.display="none";


try{

const response=await fetch("/generate",{

method:"POST",

headers:{

"Content-Type":"application/json"

},

body:JSON.stringify({

product_name,

brand,

price,

category,

features,

tone,

audience,

language

})

});

const data=await response.json();

loader.style.display="none";

document.getElementById("output").style.display="block";

document.getElementById("seo_title").value=data.seo_title;

document.getElementById("description").value=data.description;

document.getElementById("benefits").value=data.benefits;

document.getElementById("keywords").value=data.keywords;

document.getElementById("cta").value=data.cta;

}
catch(error){

loader.style.display="none";

alert("Something went wrong.");

console.log(error);

}

};


// ------------------------------
// Copy
// ------------------------------

document
.getElementById("copyBtn")
.onclick=function(){

const text=

"SEO Title\n\n"+

document.getElementById("seo_title").value+

"\n\nDescription\n\n"+

document.getElementById("description").value+

"\n\nBenefits\n\n"+

document.getElementById("benefits").value+

"\n\nKeywords\n\n"+

document.getElementById("keywords").value+

"\n\nCall To Action\n\n"+

document.getElementById("cta").value;

navigator.clipboard.writeText(text);

alert("Copied Successfully!");

};


// ------------------------------
// Download PDF
// ------------------------------

document
.getElementById("pdfBtn")
.onclick=async()=>{

const body={

seo_title:document.getElementById("seo_title").value,

description:document.getElementById("description").value,

benefits:document.getElementById("benefits").value,

keywords:document.getElementById("keywords").value,

cta:document.getElementById("cta").value

};

const response=await fetch("/download_pdf",{

method:"POST",

headers:{

"Content-Type":"application/json"

},

body:JSON.stringify(body)

});

const blob=await response.blob();

const url=window.URL.createObjectURL(blob);

const a=document.createElement("a");

a.href=url;

a.download="product_description.pdf";

a.click();

window.URL.revokeObjectURL(url);

};


// ------------------------------
// Download TXT
// ------------------------------

document
.getElementById("txtBtn")
.onclick=async()=>{

const body={

seo_title:document.getElementById("seo_title").value,

description:document.getElementById("description").value,

benefits:document.getElementById("benefits").value,

keywords:document.getElementById("keywords").value,

cta:document.getElementById("cta").value

};

const response=await fetch("/download_txt",{

method:"POST",

headers:{

"Content-Type":"application/json"

},

body:JSON.stringify(body)

});

const blob=await response.blob();

const url=window.URL.createObjectURL(blob);

const a=document.createElement("a");

a.href=url;

a.download="product_description.txt";

a.click();

window.URL.revokeObjectURL(url);

};


// ------------------------------
// Auto Focus
// ------------------------------

window.onload=function(){

document
.getElementById("product_name")
.focus();

};


// ------------------------------
// Character Counter
// ------------------------------

const featureBox=document.getElementById("features");

featureBox.addEventListener("keyup",()=>{

const len=featureBox.value.length;

document.title="Characters : "+len;

});