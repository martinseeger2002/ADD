document.addEventListener("DOMContentLoaded", function() {
    const txid = document.getElementById("txid").value;
    const imageUrl = `/content/${txid}`;
    const imgElement = document.getElementById("doginalImage");
    imgElement.src = imageUrl;

    imgElement.onload = function() {
        imgElement.style.transform = "scaleX(-1)";
        imgElement.style.filter = "invert(100%)";
    };
});
