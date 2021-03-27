'use strict';


// initializing canvas
const canvas = document.querySelector('.canvas');
const widthDocument = document.documentElement.clientWidth;
const heightDocument = document.documentElement.clientHeight;
canvas.style.width = widthDocument + 'px';
canvas.style.height = heightDocument - 100 + 'px';

const ctx = canvas.getContext('2d');
ctx.lineWidth = 1;
// changing coordinates
let transX = canvas.width * 0.5;
let transY = canvas.height * 0.5;
ctx.translate(transX, transY);

let length = 40;
let diff = 15;
let x = -20;
let y = -20;
let cube = new Cube(length, diff, x, y);


cube.draw(ctx);