/*! For license information please see 34.364f81e2.chunk.js.LICENSE.txt */
(this["webpackJsonpstreamlit-browser"]=this["webpackJsonpstreamlit-browser"]||[]).push([[34],{3892:function(t,e,s){"use strict";s.r(e),s.d(e,"default",(function(){return n}));var i=s(0),r=s.n(i),l=s(140),a=s(5);class o extends r.a.PureComponent{constructor(...t){super(...t),this.state={value:this.initialValue},this.setWidgetValue=t=>{this.props.widgetMgr.setStringValue(this.props.element,this.state.value,t)},this.onColorClose=t=>{this.setState({value:t},(()=>this.setWidgetValue({fromUi:!0})))},this.render=()=>{const t=this.props,e=t.element,s=t.width,i=t.disabled,r=this.state.value;return Object(a.jsx)(l.a,{label:e.label,help:e.help,onChange:this.onColorClose,disabled:i,width:s,value:r})}}get initialValue(){const t=this.props.widgetMgr.getStringValue(this.props.element);return void 0!==t?t:this.props.element.default}componentDidMount(){this.setWidgetValue({fromUi:!1})}}var n=o}}]);
//# sourceMappingURL=34.364f81e2.chunk.js.map