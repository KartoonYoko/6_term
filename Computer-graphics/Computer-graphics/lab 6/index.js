'use strict'


// initializing canvas
const canvas = document.querySelector('.canvas');
const widthDocument = document.documentElement.clientWidth;
const heightDocument = document.documentElement.clientHeight;
canvas.style.width = widthDocument + "px";
canvas.style.height = heightDocument - 100 + "px";

const ctx = canvas.getContext('2d');
ctx.lineWidth = 1;
// changing coordinates
let transX = canvas.width * 0.5;
let transY = canvas.height * 0.5;
ctx.translate(transX, transY);

const n = 8; // size of array
//
let arr = [];

for (let i = 0; i < n; i++){
    arr.push(new Point);
    arr[i].x = i;
    arr[i].y = i;
}

let length = 40;
let diff = 15;
let x = -20;
let y = -20;
arr[0].setPoint(x, y);
arr[1].setPoint(x, y + length)
arr[2].setPoint(x + length, y + length);
arr[3].setPoint(x + length, y);

let x1 = x + diff;
let y1 = y - diff;
arr[4].setPoint(x1, y1);
arr[5].setPoint(x1, y1 + length)
arr[6].setPoint(x1 + length, y1 + length);
arr[7].setPoint(x1 + length, y1);
//let cube = new Cube(arr);

/**
 * draw cube with 8 points
 * 
 * @param {array} arr - array of Points
 * @param {context} ctx - context of canvas 
 */
function drawCube(arr, ctx, color = 'rgb(0, 255, 255, 0.5)'){
    ctx.fillStyle = 'rgb(200, 0, 0)';
    //draw face square
    ctx.beginPath();
    ctx.moveTo(arr[0].x, arr[0].y);
    for (let i = 1; i < 4; i++){
        ctx.lineTo(arr[i].x, arr[i].y);
    }
    ctx.lineTo(arr[0].x, arr[0].y);
    ctx.closePath();
    ctx.fill();  

    //draw back square
    ctx.fillStyle = 'rgba(0, 0, 200, 0.5)';
    ctx.beginPath();
    ctx.moveTo(arr[4].x, arr[4].y);
    for (let i = 4; i < 8; i++){
        ctx.lineTo(arr[i].x, arr[i].y);
    }
    ctx.lineTo(arr[4].x, arr[4].y);
    ctx.closePath();
    ctx.fill();
    
    // draw lines
    ctx.strokeStyle = 'rgb(0, 0, 0)';
    ctx.beginPath();
    for (let i = 0; i < 4; i++){
        ctx.moveTo(arr[i].x, arr[i].y);
        ctx.lineTo(arr[i + 4].x, arr[i + 4].y);
    }
    ctx.closePath();
    ctx.stroke();
}

console.log(arr[2].x, arr[2].y);
drawCube(arr, ctx);

