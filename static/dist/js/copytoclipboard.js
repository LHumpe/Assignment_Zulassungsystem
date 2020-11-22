function Clipboard_CopyTo(value) {
  var tempInput = document.createElement("input");
  tempInput.value = value;
  document.body.appendChild(tempInput);
  tempInput.select();
  document.execCommand("copy");
  document.body.removeChild(tempInput);
}

document.querySelector('#Copy').onclick = function() {
  Clipboard_CopyTo(document.getElementById("rec-link").getAttribute("href"));

  alert("Folgender Link wurde ihrem Clipboard angehangen: \n\n" + document.getElementById("rec-link").getAttribute("href") + "\n\nBitte geben sie ihn an eine Person weiter, die für Sie ein Empfehlungsschreiben einreichen wird." );

}