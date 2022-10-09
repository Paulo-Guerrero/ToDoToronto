function submitCriteria(button){
    $.ajax({
        type: "POST",
        url: "/test",
        data: {
        "criteria" : button.id,
        "question" : button.value
        },
    })

    next_question(button.value, button.id)
}

function next_question(questionId, buttonId){
    var nextNumber = (parseInt(questionId.slice(questionId.length - 1))) + 1;
    nextQuestId = "question" + nextNumber;
    document.getElementById(buttonId).style.color = 'red';
    document.getElementById(nextQuestId).style.display = 'inline';
    document.getElementById(questionId).style.display = 'none';
}

