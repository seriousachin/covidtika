/*! For license information please see 26.2086a2f9.chunk.js.LICENSE.txt */
(this["webpackJsonpstreamlit-browser"]=this["webpackJsonpstreamlit-browser"]||[]).push([[26],{3875:function(e,t,o){"use strict";o.r(t),o.d(t,"default",(function(){return H}));var n=o(6),r=o(29),c=o(0),l=o.n(c),a=o(338),i=o(293),s=o(154);let d;!function(e){e.ASCENDING="ascending",e.DESCENDING="descending"}(d||(d={}));var h=o(8),u=o.n(h),m=o(22);const b=u()("div",{target:"e10os9ge0"})((({width:e,theme:t})=>({width:e,border:"1px solid ".concat(t.colors.secondaryBg),boxSizing:"content-box","& .table-top-right":{overflowX:"hidden",backgroundColor:t.colors.secondaryBg},"& .table-bottom-left":{overflowY:"hidden",backgroundColor:t.colors.secondaryBg}})),""),g=u()("div",{target:"e10os9ge1"})((({theme:e})=>({padding:e.spacing.sm,fontSize:e.fontSizes.smDefault,fontFamily:e.fonts.monospace,textAlign:"right",lineHeight:e.lineHeights.none})),""),f=e=>({backgroundColor:e.colors.secondaryBg,color:e.colors.fadedText60,zIndex:1}),w=e=>({overflow:"hidden",whiteSpace:"nowrap",textOverflow:"ellipsis",lineHeight:e.lineHeights.dataframeCell}),j=u()(g,{target:"e10os9ge2"})((({theme:e})=>f(e)),""),p=u()(g,{target:"e10os9ge3"})((({theme:e})=>Object(n.a)(Object(n.a)({userSelect:"none"},f(e)),w(e))),""),x=u()(g,{target:"e10os9ge4"})((({theme:e})=>Object(n.a)(Object(n.a)({userSelect:"none"},f(e)),w(e))),""),y=u()(g,{target:"e10os9ge5"})((({theme:e})=>w(e)),""),C=u()("div",{target:"e10os9ge6"})((({verticalLocator:e,horizontalLocator:t,width:o,height:n})=>({position:"absolute",[e]:"0px",[t]:"0px",width:o,height:n})),""),S=u()("div",{target:"e10os9ge7"})((({theme:e})=>({fontFamily:e.fonts.monospace,color:e.colors.darkGray,fontStyle:"italic",fontSize:e.fontSizes.smDefault,textAlign:"center"})),""),O=u()("span",{target:"e10os9ge8"})((({theme:e})=>({color:Object(m.transparentize)(e.colors.darkGray,.7),verticalAlign:"top"})),"");var N=o(116),I=o(12);const D=!("undefined"===typeof window||!window.document||!window.document.createElement);let v;function E(e){if((!v&&0!==v||e)&&D){const e=document.createElement("div");e.style.position="absolute",e.style.top="-9999px",e.style.width="50px",e.style.height="50px",e.style.overflow="scroll",document.body.appendChild(e),v=e.offsetWidth-e.clientWidth,document.body.removeChild(e)}return v}const G=(e,t,o,n)=>{const r=Object(s.c)(o),c=r.headerRows,l=r.headerCols,a=r.dataRows,i=r.cols,d=r.rows,h=25*c,u=t-2-E(),m=function(e,t,o,n,r,c){const l=25,a=e>2?200:400,i=({index:e})=>{const o=e,r=8*10/10,a=24,i=100;let s=l;for(let l=0;l<Math.min(t,i);l++){let e=-1;e=l<n?l:t>i?Math.floor(Math.random()*t):l;const d=c(o,e).contents,h=(d?d.length:0)*r+a;h>s&&(s=h)}return s};let s=[];const d=Array.from(Array(e),((e,t)=>i({index:t}))),h=d.reduce(((e,t)=>e+t),0),u=r-h,m=e=>e.filter((e=>e>a));if(u<0)s=d.map((e=>e>a?a:e));else{const e=m(d),t=u/e.length;s=d.map(((o,n)=>n in e.keys()?o+t:o))}let b=s.reduce(((e,t)=>e+t),0);if(b>r*(2/3)&&b<r){const t=(r-b)/e;s=s.map((e=>e+t)),b=s.reduce(((e,t)=>e+t),0)}const g=Math.min(b,r),f=b>r,w=({index:e})=>s[e],j=s.slice(0,o).reduce(((e,t)=>e+t));return{elementWidth:g,columnWidth:w,headerWidth:j,needsHorizontalScrollbar:f}}(i,d,l,c,u,n);let b=m.elementWidth,g=m.columnWidth,f=m.headerWidth;const w=m.needsHorizontalScrollbar;if(0===a&&b<60){b=60,f=60;let e=0;for(let t=0;t<i;t++)e+=g({index:t});e<60&&(g=()=>60/i)}const j=25*d,p=e||300,x=w?E():0;e=Math.min(j+x,p);return b+=j>p?E():0,{rowHeight:25,headerHeight:h,border:2,columnWidth:g,headerWidth:f,elementWidth:b,height:e}},R={corner:j,"col-header":p,"row-header":x,data:y};var z=o(71),W=o(69),k=o(5);function A({CellType:e,columnIndex:t,contents:o,rowIndex:n,sortedByUser:r,style:c,columnSortDirection:l,headerClickedCallback:a}){let i,s,h,u=o;const m=l===d.DESCENDING;null!=a&&0===n&&(i=()=>a(t),s="button",h=0,u=null==l?'Sort by column "'.concat(o,'"'):'Sorted by column "'.concat(o,'" (').concat(m?"descending":"ascending",")"));const b=0===n?function(e){switch(e){case d.ASCENDING:return Object(k.jsx)(O,{"data-testid":"sortIcon",children:Object(k.jsx)(W.a,{content:z.ChevronTop,size:"xs",margin:"0 twoXS 0 0"})});case d.DESCENDING:return Object(k.jsx)(O,{"data-testid":"sortIcon",children:Object(k.jsx)(W.a,{content:z.ChevronBottom,size:"xs",margin:"0 twoXS 0 0"})});default:return null}}(l):void 0;return Object(k.jsxs)(e,{style:c,onClick:i,role:s,tabIndex:h,title:u,"data-testid":e.displayName,children:[r?b:"",o]})}var H=Object(i.a)((function({element:e,height:t,width:o}){const i=l.a.useRef(null),h=Object(c.useState)(!1),u=Object(r.a)(h,2),m=u[0],g=u[1],f=Object(c.useState)(0),w=Object(r.a)(f,2),j=w[0],p=w[1],x=Object(c.useState)(d.ASCENDING),y=Object(r.a)(x,2),O=y[0],D=y[1],v=Object(s.g)(e.get("data")),E=Object(r.a)(v,2)[1],z=Object(s.c)(e),W=z.headerRows,H=z.headerCols,B=z.dataRows,L=z.cols,T=z.rows,M=e=>{let t=d.ASCENDING;j===e&&(t=O===d.ASCENDING?d.DESCENDING:d.ASCENDING),p(e),D(t),g(!0)},F=(t=>{const o=Object(s.c)(e),n=o.headerCols,r=o.dataRows,c=O!==d.DESCENDING;if(j<n||j-n>=t){const e=new Array(r);for(let t=0;t<r;t+=1)e[t]=c?t:r-(t+1);return e}return Object(s.d)(e,j-n,c)})(E),X=function({element:e,headerRows:t,sortedDataRowIndices:o}){return(n,r)=>{if(null!=o&&r>=t){const e=r-t;e>=0&&e<o.length?(r=o[e],r+=t):Object(I.d)("Bad sortedDataRowIndices ("+"rowIndex=".concat(r,", ")+"headerRows=".concat(t,", ")+"sortedDataRowIndices.length=".concat(o.length))}const c=Object(s.b)(e,n,r),l=c.contents,a=c.styles,i=c.type;return{Component:R[i],styles:a,contents:Object(N.b)(l)}}}({element:e,headerRows:W,sortedDataRowIndices:F}),J=function(e){return({columnIndex:t,key:o,rowIndex:r,style:c})=>{const l=e(t,r),a=l.Component,i=l.styles,s=l.contents,d=0===r?M:void 0,h=t===j?O:void 0,u=Object(n.a)(Object(n.a)({},c),i);return Object(k.jsx)(A,{CellType:a,columnIndex:t,rowIndex:r,style:u,contents:s,sortedByUser:m,columnSortDirection:h,headerClickedCallback:d},o)}}(X),U=G(t,o,e,X),Y=U.rowHeight,q=U.headerHeight,K=U.border,P=U.height,Q=U.elementWidth,V=U.columnWidth,Z=U.headerWidth;return setTimeout((()=>{null!=i.current&&i.current.recomputeGridSize()}),0),Object(c.useEffect)((()=>{j-H>=E&&(p(0),D(d.ASCENDING),g(!1))}),[j,H,E]),Object(k.jsxs)(b,{width:Q,className:"stDataFrame",children:[Object(k.jsx)(a.MultiGrid,{cellRenderer:J,fixedColumnCount:H,fixedRowCount:W,columnWidth:V,columnCount:L,enableFixedColumnScroll:!0,enableFixedRowScroll:!0,height:P,rowHeight:Y,rowCount:T,width:Q,classNameBottomLeftGrid:"table-bottom-left",classNameTopRightGrid:"table-top-right",hideBottomLeftGridScrollbar:!0,hideTopRightGridScrollbar:!0,ref:i}),Object(k.jsx)(C,{verticalLocator:"top",horizontalLocator:"right",width:K,height:q}),Object(k.jsx)(C,{verticalLocator:"bottom",horizontalLocator:"left",width:Z,height:K}),0===B?Object(k.jsx)(S,{children:"empty"}):null]})}))}}]);
//# sourceMappingURL=26.2086a2f9.chunk.js.map