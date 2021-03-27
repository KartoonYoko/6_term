

class Point {
    
    constructor(){
        this.x = 0;
        this.y = 0;
    }

    setPoint(x, y){
        this.x = x;
        this.y = y;
    }
}


class Cube{

    /**
     * 
     * @param {int} x 
     * @param {int} y 
     * @param {int} diff - насколько далеко задний квадра от переднего
     * @param {int} length - расстояние между точками
     */
    constructor(length, diff, x = -20, y = -20 ){
        let n = 8;

        this.arr = [];

        for (let i = 0; i < n; i++){
            this.arr.push(new Point());
        }

        this.length = length || 40;
        this.diff = diff || 15;

        this.arr[0].setPoint(x, y);
        this.arr[1].setPoint(x, y + length);
        this.arr[2].setPoint(x + length, y + length);
        this.arr[3].setPoint(x + length, y);

        let x1 = x + diff;
        let y1 = y - diff;
        this.arr[4].setPoint(x1, y1);
        this.arr[5].setPoint(x1, y1 + length);
        this.arr[6].setPoint(x1 + length, y1 + length);
        this.arr[7].setPoint(x1 + length, y1);
    }

    turnX(){

    }

    /**
     * 
     * Рисует куб
     * 
     * @param {context} ctx - context of canvas 
     */
    draw(ctx){
        ctx.fillStyle = 'rgb(200, 0, 0)';
        //draw face square
        ctx.beginPath();
        ctx.moveTo(this.arr[0].x, this.arr[0].y);
        for (let i = 1; i < 4; i++){
            ctx.lineTo(this.arr[i].x, this.arr[i].y);
        }
        ctx.lineTo(this.arr[0].x, this.arr[0].y);
        ctx.closePath();
        ctx.fill();  

        //draw back square
        ctx.fillStyle = 'rgba(0, 0, 200, 0.5)';
        ctx.beginPath();
        ctx.moveTo(this.arr[4].x, this.arr[4].y);
        for (let i = 4; i < 8; i++){
            ctx.lineTo(this.arr[i].x, this.arr[i].y);
        }
        ctx.lineTo(this.arr[4].x, this.arr[4].y);
        ctx.closePath();
        ctx.fill();
        
        // draw lines
        ctx.strokeStyle = 'rgb(0, 0, 0)';
        ctx.beginPath();
        for (let i = 0; i < 4; i++){
            ctx.moveTo(this.arr[i].x, this.arr[i].y);
            ctx.lineTo(this.arr[i + 4].x, this.arr[i + 4].y);
        }
        ctx.closePath();
        ctx.stroke();
    }

}