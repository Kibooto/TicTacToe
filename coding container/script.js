const boxes = document.querySelectorAll('.box');
const result = document.querySelector('#result');

X = 'X'
O = 'O'

let move = 0;
let game = false;

let moves = [["", "", ""],
             ["", "", ""],
             ["", "", ""]];

function appendMove(id, player) {
    let i = 0;
    let j = 0;

    if (id >= 0 && id <= 2) {
        i = 0;
        j = id;
    } else if (id >= 3 && id <= 5) {
        i = 1;
        j = id - 3;
    } else {
        i = 2;
        j = id - 6;
    }
    moves[i][j] = player;
}

let winner = ''
function checkWinner() {
    for (let i = 0; i < 3; i++) {
        if (moves[i][0] === moves[i][1] && moves[i][1] === moves[i][2] && moves[i][0] !== "") {
            winner = moves[i][0];
            return winner;
        }
    }
    for (let j = 0; j < 3; j++) {
        if (moves[0][j] === moves[1][j] && moves[1][j] === moves[2][j] && moves[0][j] !== "") {
            winner = moves[0][j];
            return winner;
        }
    }
    if (moves[0][0] === moves[1][1] && moves[1][1] === moves[2][2] && moves[0][0] !== "") {
        winner = moves[0][0];
        return winner;
    }
    if (moves[0][2] === moves[1][1] && moves[1][1] === moves[2][0] && moves[0][2] !== "") {
        winner = moves[0][2];
        return winner;
    }

    return false;
}


boxes.forEach(box => {
  box.addEventListener('click', () => {
    if (game) {
        if(box.innerHTML === '') {
            if (move % 2 === 0) {
                box.innerHTML = X
                appendMove(box.id, X)
            } else {
                box.innerHTML = O;
                appendMove(box.id, O)
            }
            move++;
            if (checkWinner()) {
                result.innerHTML = `<h2>${winner} wins!</h2>`;
                game = false
            } else if (move === 9) {
                result.innerHTML = `<h2>Draw!</h2>`;
                game = false
            } else {
                result.innerHTML = `<h2>${move % 2 === 0 ? X : O}'s turn</h2>`;
            }
            console.log(moves)
        }
    }
  })
})

function startGame() {
    modal.style.display = "block";
    console.log(modal.style.display)
}

function reset() {
    boxes.forEach(box => {
        box.innerHTML = '';
    })

    move = 0

    moves = [["", "", ""],
             ["", "", ""],
             ["", "", ""]];
    result.innerHTML = `<h2>${move % 2 === 0 ? X : O}'s turn</h2>`;
    game = true
}

const resetBtn = document.querySelector('#reset');
resetBtn.addEventListener('click', () => {
    if (resetBtn.innerHTML === 'Start') {
        startGame()
        resetBtn.innerHTML = 'Reset'
    } else {
        reset()
    }
})

const modal = document.getElementById("myModal");
const span = document.getElementsByClassName("close")[0];

span.onclick = function() {
    modal.style.display = "none";
}

window.onclick = function(event) {
  if (event.target == modal) {
    modal.style.display = "none";
  }
}
