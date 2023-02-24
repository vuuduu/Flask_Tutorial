function deleteNote(noteId) {
    fetch('/delete-note', {method: 'POST', body: JSON.stringify({ noteId: noteId })}).then((_res) => {window.location.href = "/"});
    /* 
    ANOTHER WAY TO WRITE IT SO IT'S NOT ON ONE LINE

    fetch("/delete-note", {
        method: "POST",
        body: JSON.stringify({ noteId: noteId }),
    }).then((_res) => {
        window.location.href = "/";
    });
    */
}