let controller = new ScrollMagic.Controller();
let timeline = new TimelineMax();
timeline
gsap.registerPlugin(ScrollTrigger);

const sections = document.querySelectorAll('main');
const arrow = document.querySelectorAll('main');

main.forEach(arrow => {
  gsap.fromTo(arrow.children, {y: '+=100', opacity: 0}, {y: 0, opacity: 1, stagger: 0.2, duration: 0.8, ease: 'easeInOut', scrollTrigger: {
  trigger: main,
  start: 'top 5%',
  
}})});
gsap.fromTo(".main", {opacity:0},{opacity:1 , duration:5} , {y:100},{x:-20})

