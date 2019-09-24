console.log("starting the app!");
let JSONData = "string onnsjdbkasjdkjasd";
const createCanvas = () => {
  let text = [];
  const canvasDiv = document.querySelector("#canvasDiv");
  const canvas = document.createElement("canvas");
  const clearBtn = document.getElementById("clear");
  const saveBtn = document.getElementById("btn-download");
  const describe = document.getElementById("describe");
  let canvasHeight = window.innerHeight - 100;
  let canvasWidth = window.innerWidth - 100;
  let backgroundImg;
  var clickX = new Array();
  var clickY = new Array();
  var clickDrag = new Array();
  var Imgarr = new Array();
  var maxX = [],
    minX = [],
    maxY = [],
    minY = [];
  var paint,
    startX = 0,
    startY = 0,
    described = false;

  canvas.setAttribute("id", "canvas");
  canvas.setAttribute("width", canvasWidth);
  canvas.setAttribute("height", canvasHeight);
  canvas.setAttribute("class", "border");
  canvas.setAttribute("background-color", "#cb3594");
  console.log(canvas);
  backgroundImg = prompt("ENTER YOUR DESIRED BACKGROUND");
  console.log(backgroundImg);
  canvasDiv.appendChild(canvas);
  console.log(canvas);

  if (typeof G_vmlCanvasManager != "undefined") {
    canvas = G_vmlCanvasManager.initElement(canvas);
  }
  context = canvas.getContext("2d");

  function addClick(x, y, dragging) {
    clickX.push(x);
    clickY.push(y);
    clickDrag.push(dragging);
  }

  function redraw() {
    context.clearRect(0, 0, context.canvas.width, context.canvas.height); // Clears the canvas

    context.strokeStyle = "#000";
    context.lineJoin = "round";
    context.lineWidth = 5;

    for (var i = 0; i < clickX.length; i++) {
      context.beginPath();
      if (clickDrag[i] && i) {
        context.moveTo(clickX[i - 1], clickY[i - 1]);
      } else {
        context.moveTo(clickX[i] - 1, clickY[i]);
      }
      context.lineTo(clickX[i], clickY[i]);
      context.closePath();
      context.stroke();
    }
  }

  function createobj(temp) {
    let s = clickX[startX],
      gr = s;
    for (let i = startX; i < clickX.length; i++) {
      if (s > clickX[i]) s = clickX[i];
      if (gr < clickX[i]) gr = clickX[i];
    }
    maxX.push(gr);
    minX.push(s);

    s = clickY[startY];
    gr = s;

    for (let i = startY; i < clickY.length; i++) {
      if (s > clickY[i]) s = clickY[i];
      if (gr < clickY[i]) gr = clickY[i];
    }
    minY.push(s);
    maxY.push(gr);

    var obj = {
      name: temp,
      min_X: minX[minX.length - 1],
      max_X: maxX[maxX.length - 1],
      min_Y: minY[minY.length - 1],
      max_Y: maxY[maxY.length - 1]
    };

    Imgarr.push(obj);
    console.log(Imgarr);
  }

  clearBtn.addEventListener("click", function(e) {
    context.clearRect(0, 0, context.canvas.width, context.canvas.height); // Clears the canvas
    clickX = [];
    clickY = [];
    maxX = [];
    maxY = [];
    minX = [];
    minY = [];
    startX = 0;
    startY = 0;
    clickDrag = [];
    Imgarr = [];
    text = [];
    backgroundImg = prompt("ENTER YOUR DESIRED BACKGROUND");
    console.log(`after clear button ${backgroundImg}`);
    paint = false;
  });

  saveBtn.addEventListener("click", () => {
    var dataURL = canvas.toDataURL("image/jpg", 1.0);
    let savedImg = document.getElementById("savedImg");
    savedImg.setAttribute("src", dataURL);
    saveBtn.href = dataURL;
    saveData();
  });

  describe.addEventListener("click", function(e) {
    described = true;
    var temp;
    while (true) {
      temp = prompt("Describe the sketch if completed!");
      if (temp === "") {
        alert("PLEASE DESCRIBE THE SKETCH!");
      } else {
        console.log(temp);
        if (temp !== "") {
          text.push(temp);
          console.log(`${text} array is pushed`);
        }
        break;
      }
    }

    createobj(temp);
  });

  canvas.addEventListener("mouseleave", function(e) {
    paint = false;
  });

  canvas.addEventListener("mouseup", function(e) {
    paint = false;
    described = false;
  });

  canvas.addEventListener("mousedown", function(e) {
    var mouseX = e.pageX - this.offsetLeft;
    var mouseY = e.pageY - this.offsetTop;

    paint = true;

    if (described) {
      startX = clickX.length;
      startY = clickY.length;
    }

    addClick(e.pageX - this.offsetLeft, e.pageY - this.offsetTop);
    redraw();
  });

  canvas.addEventListener("mousemove", function(e) {
    if (paint) {
      addClick(e.pageX - this.offsetLeft, e.pageY - this.offsetTop, true);
      redraw();
    }
  });
  const saveData = () => {
    JSONData = {
      background: backgroundImg,
      img: Imgarr
    };
    const jData = JSON.stringify(JSONData);
    $(function() {
      console.log("jquery");
      $.ajax({
        type: "POST",
        url: "http://localhost:8888/send",
        timeout: 2000,
        contentType: "application/json; charset=utf-8",
        dataType: "json",
        data: jData
      });
    });
  };
};

createCanvas();
