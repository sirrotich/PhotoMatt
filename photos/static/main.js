function copyImage(){
    var copyLink=document.getElementById("imageLink");

    copyLink.select();
    document.execCommand("copy");
    alert("Link Copied: " +copyLink.value);
}