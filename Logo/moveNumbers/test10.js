const element = document.querySelector(".element");

const keyframes = [
  { transform: "translate(0, 0)",           offset: 0       ,opacity:1},
  { transform: "translate(200px, 0)",       offset: 0.40    ,opacity:1},
  // { transform: "translate(200px, 200px)",   offset: 0.60    ,opacity:1},
  // { transform: "translate(0, 200px)",       offset: 0.80    ,opacity:0}
];

const options = {
  duration: 4000,
  direction: "normal",
  fill: "none",
  iterations: Infinity,
  composite:"add",
};

const animation = element.animate(keyframes, options);
