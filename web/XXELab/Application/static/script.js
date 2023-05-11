function send_data() {
    var title, desc, xmlstring;

    title = document.getElementById("title").value;
    desc = document.getElementById("desc").value;

    var xhr;
	if (window.XMLHttpRequest) {
        xhr = new XMLHttpRequest();
    } else if (window.ActiveXObject) {
        xhr = new ActiveXObject("Microsoft.XMLHTTP");
    }

    xhr.onreadystatechange = function() {
        if (xhr.readyState==4 && xhr.status==200) {
            window.location = "/";
        }
    }

    xmlstring = `<?xml version="1.0"?>
<todo>
    <title>${title}</title>
    <desc>${desc}</desc>
</todo>`;
    
    var url = "/create";

    xhr.open("POST", url, true);

    xhr.setRequestHeader("Content-Type", "text/xml");

    xhr.send(xmlstring);
}