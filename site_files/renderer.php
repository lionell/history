﻿	
maxp_somewin = 30000;
show_somewin = 1;
ison_somewin = 0;
jQuery(document).ready(function(){
	thewin = jQuery("#somewin");

	jQuery(window).scroll(function(){
		var h_doc = jQuery(document).height();
		var h_scr = jQuery(window).height();
		var horiz_pos = jQuery(this).scrollTop();
		
		if(show_somewin==1){
			if( (h_doc - (h_scr+horiz_pos) )<=maxp_somewin){
				if(ison_somewin==0){
					thewin.fadeIn("slow", function(){});
					ison_somewin = 1;
				}
			}
			else {	
				if(ison_somewin==1){					
					hide_somew(0);
				}
			}
		}
		
	});
	
function hide_somew(perm){
	if(perm==1){show_somewin = 0;}
	thewin.fadeOut("slow", function(){});
	ison_somewin = 0;
}

thewin.css("width","250px");
thewin.css("height","375px");
thewin.css("border","1px solid silver");thewin.css("box-shadow","0 0 20px 3px silver");

thewin.css("left","-10px");
thewin.css("bottom","10%");	
thewin.css("background","#fff");
	
	jQuery('#clsbtn_somewin').click(function() {
		hide_somew(1);
	});
});
