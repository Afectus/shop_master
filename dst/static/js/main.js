


function imagebasedel(id)
{
	if (confirm('Вы уверены?')) {
		$.ajax({
			type: 'GET',
			url: '/imagebase/del/'+id,
			//data: data,
			dataType: 'json',
			beforeSend: function(){},
			success: function(data){
				console.log(data);
				if(data.res == 1)
				{
					//console.log('delete goods');
					$('.imagebase'+id).remove();
				}
			},
			error: function(xhr, textStatus, errorThrown){
				console.log(errorThrown);
			}
		});
	};
	return false;
}



/* confirm action */
function jdisabled(e) {
	$(e).addClass('disabled');
	//$(e).html('Подождите'+'...');
	//$(e).html('<img src="/static/img/spinner.gif" />');
	
	var suffix = '.';
	var suffixratio = '';
	var timerId = setInterval(function() {
		console.log(suffixratio);
		suffixratio = suffixratio + suffix;
		$(e).html('Подождите'+suffixratio);
		if(suffixratio.length > 3) {
			suffixratio = '';
		}
	}, 300);
	
	console.log('jdisabled');
	return true;
} 


$(document).ready(function(){

	$("#id_aclu").chosen({
		placeholder_text_multiple: " Права",
		no_results_text: "не найдено",
		search_contains: true,
	});
	
	$("#id_executor").chosen({
		placeholder_text_multiple: " Исполнители",
		no_results_text: "не найдено",
		search_contains: true,
	});
	
	$("#id_addressee_field").chosen({
		placeholder_text_multiple: " Адресаты",
		no_results_text: "не найдено",
		search_contains: true,
	});
	
	$("#id_distributor").chosen({
		placeholder_text_multiple: " Поставщики",
		no_results_text: "не найдено",
		search_contains: true,
	});

	$("#id_user").chosen({
		placeholder_text_multiple: " Пользователи",
		no_results_text: "не найдено",
		search_contains: true,
	});

	$('.fancybox').fancybox({
		type: 'image',
		helpers: {
			overlay: {
			locked: false
			}
			}
	});


	$(function() {
		$('.chosen-select').chosen({
			search_contains: true,
			
		});
		$('.chosen-select-deselect').chosen({ allow_single_deselect: true });
	});


	$('.mydatepicker').datepicker({
		format: 'dd-mm-yyyy',
		 language: 'ru',
		 autoclose: true,
		 showOnFocus: false,
	});

	
	


	/* подсказки на кнопках сортировки */
	$('[data-toggle="tooltip"]').tooltip(); 


	/* confirm action */
	$('.jqueryconfirm, .jconfirm').click(function(){
		if (confirm('Вы уверены?')) {return true;};
		return false;
	}); 

		
	//add class form-control to input
	$('input[type=text], input[type=file], input[type=number], input[type=password], textarea, select').addClass('form-control');


	
/* 	//owl.carousel
	var owlbrand = $('.mCcarousel').owlCarousel({
		loop:true,
		margin:10,
		nav:false,
		lazyLoad:true,
		autoWidth:false,
		responsive:{
			0:{
				items:1
			},
			500:{
				items:2
			},
			1000:{
				items:6
			}
		}
	})
	//owl trigger
	$('#mCcarousel-next').click(function() {
		owlbrand.trigger('prev.owl.carousel');
	})
	$('#mCcarousel-prev').click(function() {
		owlbrand.trigger('next.owl.carousel', [300]);
	}) */
	

});  