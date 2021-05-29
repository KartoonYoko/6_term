"use strict";


class Point2D{

    constructor(x, y){
        this.x = x;
        this.y = y;
    }

    /**
     * 
     * @param {Point2D} p2D 
     */
    move(p2D){
        this.x += p2D.x;
        this.y += p2D.y;
    }
}

class Point3D{
    constructor(x, y, z){
        this.x = x;
        this.y = y;
        this.z = z;
    }

    move(p3D){
        this.x += p3D.x;
        this.y += p3D.y;
        this.z += p3D.z;
    }

    swap(p3D){
        this.x = p3D.x;
        this.y = p3D.y;
        this.z = p3D.z;
    }

    /**
     * Поворачивает точку вокруг оси (x, y, z) на угол angleGr
     * @param {*} axis - ось
     * @param {*} angleGr - угол в градусах
     */
    rotate(axis, angleGr){
        let angleRad = angleGr * Math.PI / 180;
        switch (axis)
        {
            case "x":
            {
                let tempPoint = new Point3D(
                this.x,
                this.y * Math.cos(angleRad) - this.z * Math.sin(angleRad),
                this.y * Math.sin(angleRad) + this.z * Math.cos(angleRad)
                );
                this.swap(tempPoint);
                break;
            } 
            case "y":
            {
                let tempPoint = new Point3D(
                this.x * Math.cos(angleRad) + this.z * Math.sin(angleRad),
                this.y,
                -this.x * Math.sin(angleRad) + this.z * Math.cos(angleRad)
                );
                this.swap(tempPoint);
                break;
            } 
            case "z":
            {
                let tempPoint = new Point3D(
                this.x * Math.cos(angleRad) - this.y * Math.sin(angleRad),
                this.x * Math.sin(angleRad) + this.y * Math.cos(angleRad),
                this.z
                );
                this.swap(tempPoint);
                break;
            } 
        }
    }
}

class Normal3D{
    constructor(p3D, length){
        this.point = p3D;
        this.length = length;
    }
}

class Poly{

    /**
     * arguments - 3d points
     */
    constructor(){
        let points = [];
        for(let i = 0; i < arguments.length; i++){
            points.push(arguments[i]);
        }

        this.points = points;

        // Calculating normal
        let v1 = new Point3D(points[2].x - points[1].x, points[2].y - points[1].y, points[2].z - points[1].z);
        let v2 = new Point3D(points[0].x - points[1].x, points[0].y - points[1].y, points[0].z - points[1].z);

        let normalP3D = new Point3D(v1.y*v2.z-v2.y*v1.z, v1.z*v2.x-v2.z*v1.x, v1.x*v2.y-v2.x*v1.y);
        if (points.length > 3){
            normalP3D = new Point3D(v1.y*v2.z-v2.y*v1.z, v1.z*v2.x-v2.z*v1.x, -1 * (v1.x*v2.y-v2.x*v1.y));
        }
        let normalLen = Math.sqrt(normalP3D.x*normalP3D.x + normalP3D.y*normalP3D.y + normalP3D.z*normalP3D.z);

        this.normal = new Normal3D(normalP3D, normalLen);
    }

    move(p3D){
        for(let i = 0; i < this.points.length; i++)
        {
            let point = this.points[i];
            point.move(p3D);
        }
    }

    rotate(axis, angle){
        for(let i = 0; i < this.points.length; i++)
        {
          let point = this.points[i];
          point.rotate(axis, angle);
        }
        
        this.normal.point.rotate(axis, angle);
    }

    put(ctx, center, fillColor, edgeColor){
        // Calulate visibility
        let normalAngleRad = Math.acos(this.normal.point.z/this.normal.length);
        if(normalAngleRad / Math.PI * 180 >= 90){
            return;
        }

        let lightIntensity = 1 - 2 * (normalAngleRad / Math.PI);

        ctx.fillStyle = fillColor;
        ctx.beginPath();
        for(let i = 0; i < this.points.length; i++)
        {
            let point = this.points[i];
            if(i){
                ctx.lineTo(center.x + parseInt(point.x), center.y - parseInt(point.y));
            }
            else{
                ctx.moveTo(center.x + parseInt(point.x), center.y - parseInt(point.y));
            }
        }
        ctx.fill();

        ctx.lineWidth = 1;
        ctx.strokeStyle = edgeColor;
        ctx.beginPath();
        let point = this.points[this.points.length-1];
        ctx.moveTo(center.x + parseInt(point.x), center.y - parseInt(point.y));
        for(var i = 0; i < this.points.length; i++)
        {
            let point = this.points[i];
            ctx.lineTo(center.x + parseInt(point.x), center.y - parseInt(point.y));
        }
        ctx.stroke();
    }
}

class Cube{

    /**
     * 
     * @param {*} ctx 
     * @param {*} size - размер куба
     * @param {*} fillColor - цвет полигонов
     * @param {*} edgeColor - цвет краёв
     */
    constructor(ctx, size, fillColor, edgeColor){
        this.ctx = ctx;

        let N = 6;
        let points = [];
        let R = size;
        for (let i = 0; i < N; i++){
            let angle = 2* Math.PI*i/N;
            let x = R * Math.cos(angle);
            let y = R * Math.sin(angle);
            let z = 10;
            let point = new Point3D(x, y, z);
            points.push(point);
        }
        
        let polys = [];
        polys.push(new Poly(...points));
        let point3 = new Point3D(0, 0, 2 * size);
        for (let i = 0; i < N; i++){
            let point1, point2;
            if (i == N - 1){
                point1 = points[i]
                point2 = points[0]
            }
            else{
                point1 = points[i]
                point2 = points[i + 1]
            }
            let poly = new Poly(point1, point2, point3);
            polys.push(poly);
        }
        points.push(point3);

        this.polys = polys;

        for(let i = 0; i < polys.length; i++)
        {
            points.push(polys[i].normal.point);
        }
        this.points = points;

        this.fillColor = fillColor;
        this.edgeColor = edgeColor;
        this.getColor(this.fillColor);
    }

    move(p3D){
        for(let i = 0; i < this.points.length - this.polys.length; i++)
        {
            let point = this.points[i];
            point.move(p3D);
        }
    }

    put(center){
        for(let i = 0; i < this.polys.length; i++)
        {
            let poly = this.polys[i];
            let color = this.getColor('rgb(10, 10, 10, 1)');
            let fillColor = this.setColor(color[0] * 2 * i + 10, color[1] * 2 * i + 40, color[2] * 2 * i + 60);
            poly.put(this.ctx, center, fillColor, this.edgeColor);
        }
    }

    rotate(axis, angle){
        for(let i = 0; i < this.points.length; i++)
        {
            let point = this.points[i];
            point.rotate(axis, angle);
        }
    }

    getColor(str){
        // 'rgb(0, 0, 139, 1)'
        let bracket = str.indexOf('(', 0);
        let first = str.indexOf(',', 0);
        let second = str.indexOf(',', first + 1);
        let third = str.indexOf(',', second + 1);

        let r = parseInt(str.slice(bracket + 1, first));
        let g = parseInt(str.slice(first + 1, second));
        let b = parseInt(str.slice(second + 1, third));

        return [r, g, b]
    }

    setColor(r, g, b){
        if (r > 255) r = 255;
        if (g > 255) g = 255;
        if (b > 255) b = 255;
        return 'rgb(' + r + ', ' + g + ', ' +b + ', 1)'
    }
}