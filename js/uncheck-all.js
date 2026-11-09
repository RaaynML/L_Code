//A quick script to uncheck all boxes within an iframe.
//Mostly written to uncheck the abhorrent w3schools cookie marathon.
//Draws green outlines on successful unchecks, just in case :ↄ
//The wait(125) was needed to make it fully consistent, you may
//experiment with shorter delays if your hardware is faster or
//you're more familiar with async (I'm not)

//Bookmarklet form:
javascript:void((async()=>{const wait=ms=>new Promise(resolve=>setTimeout(resolve,ms));const selector='[role="checkbox"][aria-checked="true"]';const docs=[document];for(const frame of document.querySelectorAll('iframe')){try{if(frame.contentDocument)docs.push(frame.contentDocument)}catch(e){}}for(const doc of docs){for(let attempt=0;attempt<96;attempt+=1){const box=doc.querySelector(selector);if(!box){break;}const target=box.parentElement??box;target.style.outline='3px outset rgb(64 222 0)';target.style.outlineOffset='3px';box.focus({preventScroll:true});box.click();await wait(125);if(box.isConnected&&box.getAttribute('aria-checked')==='true'){const view=doc.defaultView;box.dispatchEvent(new view.KeyboardEvent('keydown',{key:' ',code:'Space',bubbles:true,cancelable:true}));box.dispatchEvent(new view.KeyboardEvent('keyup',{key:' ',code:'Space',bubbles:true,cancelable:true}));await wait(200)}if(box.isConnected&&box.getAttribute('aria-checked')==='true'){target.style.outline='4px inset rgb(96 222 8)';console.warn('Could not change checkbox:',box);break;}}}let remaining=0;for(const doc of docs){remaining+=doc.querySelectorAll(selector).length;}console.log('Remaining checked boxes:',remaining)})());

//Readable form:
(async() =>{
	const wait = ms => new Promise(resolve => setTimeout(resolve, ms));
	const selector = '[role="checkbox"][aria-checked="true"]';
	const docs = [document];
	for(const frame of document.querySelectorAll('iframe')){
		try{ if(frame.contentDocument){docs.push(frame.contentDocument)} } catch (e){}
	}
	for(const doc of docs){
		for(let attempt = 0; attempt < 96; attempt += 1){
			const box = doc.querySelector(selector);
			if(!box){ break; }
			const target = box.parentElement ?? box;
			target.style.outline = '3px outset rgb(64 222 0)';
			target.style.outlineOffset = '3px';
			box.focus({preventScroll:true});
			box.click();
			await wait(125);
			if(box.isConnected && box.getAttribute('aria-checked') === 'true'){
				const view = doc.defaultView;
				box.dispatchEvent(new view.KeyboardEvent('keydown',{
					key: ' ', code: 'Space', bubbles: true, cancelable: true
				}));
				box.dispatchEvent(new view.KeyboardEvent('keyup',{
					key: ' ', code: 'Space', bubbles: true, cancelable: true
				}));
				await wait(200)
			}
			if(box.isConnected && box.getAttribute('aria-checked') === 'true'){
				target.style.outline = '4px inset rgb(96 222 8)';
				console.warn('Could not change checkbox:', box);
				break;
			}
		}
	}
	let remaining = 0;
	for(const doc of docs){ remaining += doc.querySelectorAll(selector).length;	}
	console.log('Remaining checked boxes:', remaining)
})();
