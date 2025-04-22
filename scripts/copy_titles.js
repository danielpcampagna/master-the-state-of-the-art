function copy(text) {
    var input = document.createElement('textarea');
    input.innerHTML = text;
    document.body.appendChild(input);
    input.select();
    var result = document.execCommand('copy');
    document.body.removeChild(input);
    return result;
}

copy(Array.from(document.querySelectorAll("h3 a")).map(e => e.innerText).join("\n"))