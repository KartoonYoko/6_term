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
 * @param {*} x  - с какого пикселя начать
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
 * @param {*} x - с какого пикселя начать по Х
 * @param {*} y - с какого пикселя начать по Y 
 * @param {*} width - cколько пикселей по ширине взять
 * @param {*} height - по высоте
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
 * Применяет фильтр к битмапу
 * 
 * @param {*} bitmap - bitmap NxN
 * @param {*} filter - filter MxM пока фильтр только 3x3 
 * @param {*} filterNumber - float
 */
function filterBitmap(filterNumber, bitmap, filter){
    let sizeOfBitmap = bitmap.length;
    let sizeOfFilter = filter.length;
    for (let i = 1; i < sizeOfBitmap - 1; i++){
        for (let j = 1; j < sizeOfBitmap - 1; j++){
            // получим битмап размера фильтра для переумножения
            let bitmapArr = [];
            for (let k = i - 1; k < i + sizeOfFilter - 1; k++){     // TODO: для любого размера фильтра
                let bufArr = [];
                for (let h = j - 1; h < j + sizeOfFilter - 1; h++){     // TODO: для любого размера фильтра
                    bufArr.push(bitmap[k][h]);
                }
                bitmapArr.push(bufArr);
            }

            let res = MultiplyMatrix(bitmapArr, filter);
            res = multMatrixNumber(filterNumber, res);
            // Внесем изменения
            let count1 = 0;
            for (let k = i - 1; k < i + sizeOfFilter - 1; k++){     // TODO: для любого размера фильтра
                let count2 = 0;
                for (let h = j - 1; h < j + sizeOfFilter - 1; h++){     // TODO: для любого размера фильтра
                    bitmap[k][h] = res[count1][count2];
                    count2++;   
                }
                count1++;
            }      
        }
    }
}


function colorBitmap(bitmap){
    let sizeOfBitmap = bitmap.length;
    for (let i = 1; i < sizeOfBitmap - 1; i++){
        for (let j = 1; j < sizeOfBitmap - 1; j++){
            bitmap[i][j] = [0, 0, 0];
        }
    }
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
    let widthBitmap = 500;
    let heightBitmap = 500;
    bitmap1 = getBitmap(ctx, 0, 0, widthBitmap, heightBitmap);
    // console.log(bitmap1);
    // let bm = filterBitmap(1 / n, bitmap1, arr);
    filterBitmap(1 / (n), bitmap1, arr);
    // console.log(bitmap1);
    // colorBitmap(bitmap1);
    fillRectWithBitmap(ctx, bitmap1, 0, 0);
}





