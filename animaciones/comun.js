// Utilidades comunes de las animaciones programadas (una función render(t) por página, sin animaciones CSS).
const $=id=>document.getElementById(id);
const clamp=(x,a=0,b=1)=>Math.min(b,Math.max(a,x)), seg=(t,a,b)=>clamp((t-a)/(b-a)), lerp=(a,b,u)=>a+(b-a)*u;
const E={out:u=>1-Math.pow(1-u,3), out5:u=>1-Math.pow(1-u,5), inn:u=>u*u,
  io:u=>u<.5?4*u*u*u:1-Math.pow(-2*u+2,3)/2,
  back:u=>{const c=1.9,c3=c+1;return 1+c3*Math.pow(u-1,3)+c*Math.pow(u-1,2)},
  spring:u=>u>=1?1:1-Math.exp(-6.5*u)*Math.cos(7.5*u)};
function rng(a){return()=>{a|=0;a=a+0x6D2B79F5|0;let t=Math.imul(a^a>>>15,1|a);t=t+Math.imul(t^t>>>7,61|t)^t;return((t^t>>>14)>>>0)/4294967296}}
const miles=n=>String(Math.round(n)).replace(/\B(?=(\d{3})+(?!\d))/g,'.'), dec=x=>x.toFixed(1).replace('.',',');
const show=(el,on)=>{el.style.display=on?'block':'none'};
// entradas habituales
const pop=(el,t,t0,d=.36,dy=40)=>{const u=seg(t,t0,t0+d);el.style.opacity=clamp(u*3);el.style.transform=`translateY(${dy*(1-E.out5(u))}px) scale(${lerp(.6,1,E.back(u))})`};
const sube=(el,t,t0,d=.4,dy=24)=>{const u=E.out5(seg(t,t0,t0+d));el.style.opacity=u;el.style.transform=`translateY(${dy*(1-u)}px)`};
// trazo de rotulador: trazo(path) lo prepara; dib(path,u) lo dibuja de 0 a 1
const trazo=p=>{p._L=p.getTotalLength();p.style.strokeDasharray=p._L;p.style.strokeDashoffset=p._L;return p};
const dib=(p,u)=>{p.style.strokeDashoffset=p._L*(1-u);p.style.opacity=u>0?1:0};
const fuentes=async()=>{await Promise.all([document.fonts.load('400 100px Anton'),document.fonts.load('800 40px Mont'),document.fonts.load('700 40px Kalam')]);await document.fonts.ready};
// fondo de vídeo real (una cuenta sobre un panel quieto aburre): fotogramas de img/bg/<clave>/ (fondos.py) en un
// canvas, a 0,6x, de ida y vuelta, desenfocados y oscurecidos, con un empuje lento
const fondoVideo=(canvas,clave,{blur=8,brillo=.5}={})=>{const N=(window.FONDOS||{})[clave]||0, ims=[];
  for(let k=1;k<=N;k++){const im=new Image(); im.src=`img/bg/${clave}/${String(k).padStart(4,'0')}.jpg`; ims.push(im)}
  const cx=canvas.getContext('2d');
  return {N, listo:()=>Promise.all(ims.map(im=>im.decode().catch(()=>0))),
    pinta:(t,dur)=>{if(!N)return; const per=Math.max(1,2*N-2), f=Math.floor(Math.max(0,t)*18)%per, im=ims[f<N?f:per-f];
      if(!im||!im.naturalWidth)return; const z=1.08+.07*seg(t,0,dur), s=Math.max(1920/im.naturalWidth,1080/im.naturalHeight)*z;
      const w=im.naturalWidth*s, h=im.naturalHeight*s; cx.filter=`blur(${blur}px) brightness(${brillo}) saturate(.9)`;
      cx.drawImage(im,(1920-w)/2+30*Math.sin(t*.25),(1080-h)/2,w,h); cx.filter='none'}}};
