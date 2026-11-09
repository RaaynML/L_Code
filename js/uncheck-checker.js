//! See & use after uncheck-all.js
//An alert box that verifies the state of checkboxes.
//All zeroes are good.

//bookmarket form:
javascript:void(()=>{const frames=[...document.querySelectorAll('iframe')];let total=0;for(const frame of frames){try{total+=frame.contentDocument.querySelectorAll('[role="checkbox"][aria-checked="true"]').length;}catch(e){}}alert('Top-level boxes: '+document.querySelectorAll('[role="checkbox"][aria-checked="true"]').length+'\nSame-origin iframe boxes: '+total+'\nIframes: '+frames.length)})()

//readable form:
(()=>{
	const frames = [...document.querySelectorAll('iframe')];
	let total = 0;
	for(const frame of frames){
		try{
			total += frame.contentDocument.querySelectorAll('[role="checkbox"][aria-checked="true"]').length;
		} catch(e){}
	}
	alert('Top-level boxes: ' + document.querySelectorAll('[role="checkbox"][aria-checked="true"]').length + '\nSame-origin iframe boxes: '+total + '\nIframes: '+frames.length);
})();
