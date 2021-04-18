'use strict';
/**
 * 12 laba
 * 
 * python -m http.server
 * localhost:8000
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

/**
 * Закрасить, используя битмап
 * @param {*} ctx 
 * @param {*} b 
 * @param {*} x 
 * @param {*} y 
 */
function fillRectWithBitmap(ctx, b, x, y){

    for (let i = 0; i < b.length; i++){
        for (let j = 0; j < b[0].length; j++){
            setPixel(ctx, x + i, y + j, b[i][j]);
        }
    }
}

/**
 * Возвращает битмап прямоугльника
 * 
 * @param {*} ctx 
 * @param {*} x 
 * @param {*} y 
 * @param {*} width 
 * @param {*} height 
 * @returns {Array} arr
 */
function getBitmap(ctx, x, y, width, height){

    let arr = new Array();
    for (let i = 0; i < height; i++){
        let a = new Array();
        for (let j = 0; j < width; j++){
            let data = ctx.getImageData(x + i, y + j, 1, 1).data;
            a.push([data[0], data[1], data[2]]);
        }
        arr.push(a);
    }
    return arr;
}

/**
 * Умножение битмапа на число
 * 
 * @param {*} a 
 * @param {*} A 
 * @returns 
 */
function multMatrixNumber(a,A)  // a - число, A - bitmap (двумерный массив)
{   
    var m = A.length, n = A[0].length, B = [];
    for (var i = 0; i < m; i++)
    { 
        B[i] = [];
        for (var j = 0; j < n; j++)
        {
            B[i][j] = [0, 0, 0]
            for (let q = 0; q < 3; q++)
                B[i][j][q] = Math.round(a*A[i][j][q]);
        }
    }
    return B;
}


/**
 * // Умножение матрицы и битмапа
 * 
 * @param {*} A - битмап
 * @param {*} B - матрица
 * @returns битмап
 */
function MultiplyMatrix(A,B)
{
    var rowsA = A.length, colsA = A[0].length,
        rowsB = B.length, colsB = B[0].length,
        C = [];
    if (colsA != rowsB) return false;
    for (var i = 0; i < rowsA; i++) C[i] = [];
    for (var k = 0; k < colsB; k++)
    { 
        for (var i = 0; i < rowsA; i++)
        { 
            var t = [0, 0, 0];
            for (var j = 0; j < rowsB; j++){
                for (let q = 0; q < 3; q++)
                    t[q] += A[i][j][q]*B[j][k];
            }
            C[i][k] = t;
        }
    }
    return C;
}

/**
 * Применяет фильтр
 * 
 * @param {*} b - bitmap
 * @param {*} a - filter
 */
function filterBitmap(k, b, a){
    let res = MultiplyMatrix(b, a);
    console.log(b);
    console.log(res);
    res = multMatrixNumber(k, res);
    return res;
}

const CANVAS_WIDTH = 1500;
const CANVAS_HEIGHT = 800;

const canvas = document.querySelector('.canvas');
canvas.width = CANVAS_WIDTH;
canvas.height = CANVAS_HEIGHT;
const ctx = canvas.getContext('2d');
let bitmap1 = [];

let img1 = document.getElementById("photo1");

let isImgloaded = false;
img1.onload = function(){
    let x = -400;
    let y = -400;
	ctx.drawImage(img1, x, y);
    
    let n = 3;
    let arr = [];
    for (let i = 0; i < n; i++){
        let a = new Array();
        for (let j = 0; j < n; j++){
            a.push(1);
        }
        arr.push(a);
    }
    let xBitmap = 10;
    let yBitmap = 10;
    bitmap1 = getBitmap(ctx, xBitmap, yBitmap, n, n);
    let bm = filterBitmap(1 / n, bitmap1, arr);
    // console.log(bitmap1);
    // console.log(bm);
    fillRectWithBitmap(ctx, bm, xBitmap, yBitmap);
}





