AOS.init({
    duration: 800,
    easing: "ease-in-out"
});
let section=document.querySelector('.hero')
const options={
    threshold:0.5,
    rootMargin:'48px'
    
}
const scroll_observer=new IntersectionObserver((enteries1,scroll_observer)=>{
    enteries1.forEach(e=>{
        console.log(e.intersectionRatio)
        let header=document.querySelector('.navbar')
      
   
        if(!e.isIntersecting){
            header.style.backgroundColor='#191d1d'
            header.style.color='white'
        }
        else{
            header.style.backgroundColor='transparent'
            header.style.color='white'
        }
        
    })
},options)

scroll_observer.observe(section)

let hero=document.querySelector('.hero h1')
console.log(hero)
document.addEventListener('scroll',function(e){
    
    hero.style.marginTop=(0.5*window.scrollY)+'px'

})