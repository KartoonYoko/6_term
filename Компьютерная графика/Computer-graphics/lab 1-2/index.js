'use strict'


/**
 * Симметричный цифровой дифференциальный анализатор
 * @param {points} points
 * @param {*} arr нулевая матрица
 */
function singleEndedDDA(points, arr){
    let x1 = points.x1;
    let y1 = points.y1;
    let x2 = points.x2;
    let y2 = points.y2;
    let px = x2 - x1;
    let py = y2 - y1;
    

    let len = arr.length;

    arr[x1][y1] = 1;

    if (Math.abs(px) >= Math.abs(py)){
        let k = py / px;
        if (x1 <= x2){
            while(x1 < x2){
                x1++;
                y1 += k;

                if (y1 < len) {
                    arr[x1][Math.trunc(y1)] = 1;
                }
            }
        }else{
            while(x1 > x2){
                x1--;
                y1 -= k;

                if (y1 < len) {
                    arr[x1][Math.trunc(y1)] = 1;
                }
            }
        }
    }else{
        let k = px / py;
        if (y1 >= y2){
            while(y1 > y2){
                y1--;
                x1 -= k;

                if (x1 < len) {
                    arr[Math.trunc(x1)][y1] = 1;
                }
            }
        }else{
            while(y1 < y2){
                y1++;
                x1 += k;

                if (x1 < len) {
                    arr[Math.trunc(x1)][y1] = 1;
                }
            }
        }
    }

    let canvas = document.querySelector('.canvas');

    let i = 0;
    let j = 0;
    for (let node of canvas.childNodes) {
        if (arr[i][j] == 1){
            node.classList.add('colored');
        }
        if (i == len - 1){
            i = 0; 
            j++;
        }
        else { i++; }
        
    }
}

/**
 * 
 * @param {points} points 
 * @param {*} arr 
 */
function bresenhamDDA(points, arr){
    let x1 = points.x1;
    let y1 = points.y1;
    let x2 = points.x2;
    let y2 = points.y2;
    let px = x2 - x1;
    let py = y2 - y1;
    let e = 2 * py - px;
    let l = px;

    let len = arr.length;

    arr[x1][y1] = 1;

    
    if (Math.abs(px) >= Math.abs(py)){
        if (y1 <= y2){
            for (let i = 0; i < l; i++) 
            {
                if (e >= 0) 
                {
                    x1 += 1;
                    y1 += 1;
                    e += 2 * (py - px);
                }
                else x1 += 1;
                e += 2 * py;
                arr[x1][y1] = 2;
            }
            console.log('1');
        }
        else{
            console.log('2 ');
            for (let i = 0; i < l; i++) 
            {
                if (e <= 0) 
                {
                    x1 += 1;
                    y1 -= 1;
                    e += 2 * (py - px);
                }
                else x1 += 1;
                console.log(e);
                e += 2 * py;
                arr[x1][y1] = 2;
            }
            
        }
    }

    let canvas = document.querySelector('.canvas');

    let i = 0;
    let j = 0;
    for (let node of canvas.childNodes) {
        if (arr[i][j] == 2){
            node.classList.add('colored-brs');
        }
        if (i == len - 1){
            i = 0; 
            j++;
        }
        else { i++; }
        
    }
}

/**
 * 
 * @param {event} event 
 * @param {points} points 
 */
function markPixel(event, points, n){
    event.currentTarget.classList.toggle('marked');
    let canvas = document.querySelector('.canvas');

    let i = 0;
    let j = 0;
    for (let node of canvas.childNodes) {

        if (node.classList.contains('canvas__pixel')){
            
            if (node === event.currentTarget) { 

                if(points.isFull()){    // если уже имеется две точки нужно удалить одну из них
                    let delPoints = points.getPrevChanged();

                    let i = 0;
                    let j = 0;
                    for (let node of canvas.childNodes){

                        if (i == delPoints.x && j == delPoints.y){
                            node.classList.toggle('marked');
                        }

                        if (i == n - 1){
                            i = 0; 
                            j++;
                        }
                        else { i++; }

                        
                    }
                    
                }

                points.fillPoints(i, j);

                break; 
            }

            if (i == n - 1){
                i = 0; 
                j++;
            }
            else { i++; }

        }
    }
}

function fillCanvas(n){
    let canvas = document.querySelector('.canvas');
    for(let i = 0; i < n; i++){
        let pixel = document.createElement("div");
        pixel.classList.add("canvas__pixel");
        pixel.addEventListener('click', () => markPixel(event, points, 30));

        canvas.append(pixel);
    }
}

let points = {
    x1 : null,
    y1 : null,
    x2 : null,
    y2 : null,
    changed : null,

    setFirst(v1, v2){
        this.x1 = v1;
        this.y1 = v2;
        this.changed = 1;
    },

    setSecond(v1, v2){
        this.x2 = v1;
        this.y2 = v2;
        this.changed = 2;
    },

    fillPoints(v1, v2){
        if (this.isFull()){
            if(this.changed == 1){
                this.setSecond(v1, v2);
            }
            else{
                this.setFirst(v1, v2);
            }
        }else{
            if (this.isFirstPointFull()) this.setSecond(v1, v2);
            else this.setFirst(v1, v2);
        }
    },
    isFirstPointFull(){
        if (this.x1 != null && this.y1 != null) return true;
        else return false;
    },
    isSecondPointFull(){
        if (this.x2 != null && this.y2 != null) return true;
        else return false;
    },
    isFull(){
        if (this.x1 != null && this.x2 != null && this.y1 != null && this.y2 != null){
            return true
        }
        else{ return false; }

    }, 
    getPrevChanged(){
        if (this.changed == 1)   
            return { x : this.x2, y : this.y2 }
        else
            return { x : this.x1, y : this.y1 }
    }
}

let n = 30;
fillCanvas(n*n);

let arr = new Array(30);

for (let i = 0; i < n; i++){
    let buf = new Array(30);
    for(let j = 0; j < n; j++){
        buf[j] = 0;
    }
    arr[i] = buf;
}

let btn = document.querySelector('.btn');
btn.addEventListener('click', () => singleEndedDDA(points, arr));

let btnBres = document.querySelector('.btn-bres');
btnBres.addEventListener('click', () => bresenhamDDA(points, arr));