'use strict';
/**
 * 16 laba
 * 
 */



/**
 * Закрасить пиксель
 * 
 * @param {*} ctx 
 * @param {Array} color
 */
function setPixel(ctx, x, y, color){
    let c = "rgb(" + color[0] + ", " + color[1] + ", " + color[2] + ")";
    // console.log(c);
    ctx.fillStyle = c;
    ctx.fillRect( x, y, 1, 1 );
}



const CANVAS_WIDTH = 1500;
const CANVAS_HEIGHT = 800;

const canvas = document.querySelector('.canvas');
canvas.width = CANVAS_WIDTH;
canvas.height = CANVAS_HEIGHT;
const ctx = canvas.getContext('2d');

