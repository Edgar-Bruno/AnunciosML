$(document).ready(function () {
    // Code adapted from http://djangosnippets.org/snippets/1389/  
    function updateElementIndex(el, prefix, ndx) {
        var id_regex = new RegExp('(' + prefix + '-\\d+-)');
        var replacement = prefix + '-' + ndx + '-';
        if ($(el).attr("for")) $(el).attr("for", $(el).attr("for").replace(id_regex,
        replacement));
        if (el.id) el.id = el.id.replace(id_regex, replacement);
        if (el.name) el.name = el.name.replace(id_regex, replacement);

        /* ADD form sem duplicar valor do textCounter do item anterior */
        if (el.id.indexOf('LAB') > -1){
            document.getElementById((el.id).toString()).innerHTML = '';
        }
       
        /* Esconder form ADD e desseleciona checkbox. Isso só ocorre no primeiro formset */
        if (el.id.search(/_default\b/i) != -1){

            var checkBox = document.getElementById(el.id.replace("_default","_checkBox")).querySelectorAll('.checkBoxADD');
        
            if(checkBox[0].checked){
               checkBox[0].checked = false;
               slideToggle(document.getElementById(el.id.replace("_default", "")));
              
            }
        }
    }

    function deleteForm(btn, prefix) {

        var formCount = parseInt($('#id_' + prefix + '-TOTAL_FORMS').val());

        if (formCount > 1) {
            // Delete the item/form
            $(btn).parents('.item').remove();
            var forms = $('.item'); // Get all the forms  
            // Update the total number of forms (1 less than before)
            // Correction: TOTAL_FORM This way does not erase the last form item
            //$('#id_' + prefix + '-TOTAL_FORMS').val(forms.length);
            var i = 0;
            // Go through the forms and set their indices, names and IDs
            for (formCount = forms.length; i < formCount; i++) {
                $(forms.get(i)).children().children().each(function () {
                              
                    if ($(this).attr('type') == 'text'){
                      
                        updateElementIndex(this, prefix, i);
                    };
                });
            }
        } // End if
        else {
            alert("You have to enter at least one todo item!");
        }

        if ( formCount == 1 ){
            var rmLink = document.getElementById('remove');
            rmLink.style.visibility = 'hidden';
        }
        return false;
    }

    function addForm(btn, prefix) {

        var forms = $('.item');

        // You can only submit a maximum of 10 todo items 
        if (forms.length < 10) {

            var formCount = parseInt($('#id_' + prefix + '-TOTAL_FORMS').val());
            
            // Clone a form (without event handlers) from the first form
            var row = $(".item:first").clone(false).get(0);
            // Insert it after the last form
            $(row).removeAttr('id').hide().insertAfter(".item:last").slideDown(300);

            // Remove the bits we don't want in the new row/form
            // e.g. error messages
            $(".errorlist", row).remove();
            $(row).children().removeClass("error");

            // Relabel or rename all the relevant bits
            $(row).children().children().each(function () {
                updateElementIndex(this, prefix, formCount);

                //$(this).val("");
                var el = document.getElementById(this.id);
                $(el).val("");

            try {
                // Captura apenas o número do formset ATUALIZADO - Valido
                var r = /\d+/;
                var valorFV = (this.id.match(r));

                var formIDinv = document.getElementById(this.id).getElementsByTagName('*');
                console.log(formIDinv);
   
                for (var i =0; i < formIDinv.length; i++){
                    // Captura apenas o número do formset DESATUALIDO - Inválido
                    if (formIDinv[i].id){
                        var valorFI = (formIDinv[i].id.match(r));
                        console.log("ORIGINAL "+formIDinv[i].id);

                        formIDinv[i].id = formIDinv[i].id.replace(valorFI, valorFV);

                    }
                        
                    console.log("SOBRESCR "+formIDinv[i].id+" - "+formIDinv[i].name);
                    if (formIDinv[i].name){
                        formIDinv[i].name = formIDinv[i].name.replace(valorFI, valorFV);
                    }
                    if (formIDinv[i].id.search(/ADD\b/i) != -1){
                            formIDinv[i].value=null;
                    }
                }//end for

                if (el.id.search(/btn\b/i) != -1){
                    el.setAttribute('data-element', "#"+el.id.replace("btn", ""));
                    }

                }
            catch(err){

                console.log("Renomear CAMPOS "+err)
            }
    
            });

            // Add an event handler for the delete item/form link 
            $(row).find(".delete").click(function () {
           
                return deleteForm(this, prefix);
            });
            // Update the total form count
            $("#id_" + prefix + "-TOTAL_FORMS").val(formCount + 1);
            
            /*  Apenas no firefox
            alert(x.toSource());
            */
        } // End if
        else {
            alert("Sorry, you can only enter a maximum of ten items.");
        }
        return false;
    }
    // Register the click event handlers
    $("#add").click(function () {

        var rmElemente = document.getElementById('remove');
        rmElemente.style.visibility = 'visible';
        return addForm(this, "form");
    });

    $(".delete").click(function () {
        return deleteForm(this, "form");
    });
});

//Contador de caracteres

function textCounter(field, maxLimit) {

var count = (maxLimit - field.value.length)

if(field.value.length >= maxLimit){

    field.value = field.value.substring(0, maxLimit);

}

if (document.getElementById(field.id+"LAB") == undefined){

    var labelCount = document.createElement("p");
    var txt = document.createTextNode(count + " caracteres restantes.");
    labelCount.appendChild(txt);
    labelCount.id = field.id+"LAB";

    //document.getElementById(field.id).before(labelCount);

    var item =  document.getElementById(field.id);

    item.parentNode.insertBefore(labelCount, item.nextSibling);

    }
else{
    document.getElementById(field.id+"LAB").innerHTML = count +" caracteres restantes.";
    }
}

/* imagem prévisualização */

function ImageChange(ele){

    function handleIMGsSelect(evc) {

        var files = evc.target.files;

        try {
            files[0].name;
        }
        catch(err){

            if (document.getElementById(ele.id+"_LAB") == undefined){

                var labelP = document.createElement("p");
                var txt = document.createTextNode("Insira uma imagem.");
                labelP.appendChild(txt);
                labelP.setAttribute('class', "inserirTXT");
                labelP.id = ele.id+"_LAB";

                document.getElementById(ele.id+"_DIV").appendChild(labelP);

            }

            var img = document.getElementById(ele.id+"_IMG");
            img.style.display = 'none';
            img.setAttribute('src', '')
        }

        var reader = new FileReader();

        reader.onload = (function(fileChange) {
            return function(e){

                if (document.getElementById(ele.id+"_LAB") != undefined){
                    document.getElementById(ele.id+"_LAB").remove();
                }

                var img = document.getElementById(ele.id+"_IMG");
                img.style.display = 'block';
                img.setAttribute('src', e.target.result);
                img.setAttribute('class', 'thumb');

                // REMOVE A LISTA DE EVENTOS
                document.getElementById(ele.id+"_DIV").removeEventListener('change', handleIMGsSelect, false);

                };

        })(evc.target.files[0]);

        try{
        
        reader.readAsDataURL(evc.target.files[0]);
         
        }
        finally{
        return null;
       }
      }// function

      //alert('SIM '+document.getElementsByName(id+"Inp").length+" "+document.getElementById(id+"Inp").name)

      document.getElementById(ele.id+"_DIV").addEventListener('change', handleIMGsSelect, false);
      
}

/* imagem prévisualização */

function ImageADD(ele){

    function handleFileSelect(evt) {

    //Verifica e Substitui todas as imagens preselecionadas
    if (document.getElementById("img_"+ele.id) == undefined){

        document.getElementById(ele.id+"_LAB").innerHTML = "Substitua as imagens selecionadas";

    }
    else{

    // remove todos os elementos
      var elementos = document.getElementsByClassName("thumbF").length;
    /*
      for(var x in elementos){
        alert("valores"+elementos[x].name)

      }
    */
    for (var i = 0; i< elementos; i++ ){
       document.getElementById("img_"+ele.id).remove();
      }

    }

        var files = evt.target.files; // FileList object

        // Loop through the FileList and render image files as thumbnails.
        for (var i = 0, f; f = files[i]; i++) {

              var reader = new FileReader();

              // Closure to capture the file information.
              reader.onload = (function(theFile) {
                return function(e) {
                  // Render thumbnail.

                  var img = document.createElement("img");
                  img.id ="img_"+ele.id;
                  img.setAttribute('src', e.target.result);
                  img.setAttribute('title', theFile.name);
                  img.setAttribute('class', "thumbF");

                  document.getElementById('list').appendChild(img);

                };
              })(f);
              // Read in the image file as a data URL.
              reader.readAsDataURL(f);
       
        }// end for
      // REMOVE A LISTA DE EVENTOS
      document.getElementById(ele.id).removeEventListener('change', handleFileSelect, false);

      }

  document.getElementById(ele.id).addEventListener('change', handleFileSelect, false);
}

function slideToggle(el){

    elST = $(el).data('element');

    try{
        // Condição para link ADD itens no forumário | retorna o checkbox do item
        var checkBox = document.getElementById(el.id+"_checkBox").querySelectorAll('.checkBoxADD');
        var str = elST.toString();
        var r = str.replace(/#/i, "");

        elDefault = document.getElementById(el.id+"_default");

        if(checkBox[0].checked){
           // console.log("visible");
            if (document.getElementById(r).style.display){
                $(elST).slideToggle();
                $(elDefault).slideToggle();
            }
            
        }
        else{
           // console.log("hidden");
            if (!document.getElementById(r).style.display){
                $(elST).slideToggle();
                $(elDefault).slideToggle();
            }
        }
    }
    catch(err){
        console.log("el "+ err + "--- "+el.id);
        var btn = document.getElementById(el.id);
        var divEle = document.getElementById(el.id).parentNode;// Pega a div do elemento inserido
        // Condição para link exibir itens cadastrados
        if ($('#'+el.id).text().indexOf('Mostrar') > -1){

                divEle.id = divEle.id+"_o";
                btn.setAttribute('class', "botao botaoOcult");
                btn.firstChild.data = "Ocultar";
                $(elST).slideDown("slow");
                
        }
        else{
                btn.setAttribute('class', "botao botaoDef");
                btn.firstChild.data = "Mostrar";
                $(elST).slideUp("slow");

                var str = divEle.id.toString();
                var r = str.replace(/_o/i, "");
                divEle.id = r;

        }

    }

}

var timer;
$(".slideToggle_aux").mouseenter(function() {
    var el = $(this).data('element');
    timer = setTimeout(function(){
        $(el).slideDown("slow");
    }, 1000);
}).mouseleave(function() {
    var el = $(this).data('element');
    $(el).slideUp("slow");
    clearTimeout(timer);
});


function checkedCeckBox(){
    // Manter item ADD checked visível
    var elementos = document.getElementsByClassName("linkADD");

   for (var i = 0; i< elementos.length; i++ ){

        //console.log(" _checkBox "+ elementos[i].id);
        
        var checkBox = document.getElementById(elementos[i].id+"_checkBox").querySelectorAll('.checkBoxADD');
        
        if(checkBox[0].checked){
            
            elDefault = document.getElementById(elementos[i].id+"_default");
            $(elDefault).slideToggle();

            el = $(elementos[i]).data('element');
            $(el).slideToggle();
        }
    }
}
/*modal*/

// Get the modal
function Modal(est_ved, nav, url){

    var modalDiv = document.createElement("div");
    modalDiv.id = "modalJanela";
    modalDiv.setAttribute('title', est_ved+" : "+nav);

    var iframeModal = document.createElement("iframe");
    iframeModal.setAttribute('frameBorder', "0");
    iframeModal.setAttribute('height', "95%");
    iframeModal.setAttribute('width', "100%");
    iframeModal.setAttribute('src', url);

    modalDiv.appendChild(iframeModal);
  
    document.getElementById('modalDiv').appendChild(modalDiv);

    $(function() {
        
        $("#modalJanela" ).dialog({
          modal: true,
          width: 500,
          height: 425,
          closeText: "Xis",
          show: {
                    effect: "fade",
                    duration: 250
          },
          hide: {
                    effect: "fade",
                    duration: 250
          },
          open: function() {
            $('.ui-widget-overlay').addClass('custom-overlay');
          },
          close: function() {
            $('.ui-widget-overlay').removeClass('custom-overlay');
              modalDiv.remove();
          },

        });
  });
}

// Calendário

/* Include the jquery Ui here */
$(function(){

    $( "#datepicker" ).datepicker({
        changeMonth: true,
        changeYear: true,
        language: 'pt-BR',
        minViewMode: 0,
        yearRange: '1977:' + new Date().getFullYear(),
        dateFormat: 'yy-mm-dd' }).val();

});
/* autocomplete*/
function AutoComplete(el, arg, argb){

    $("#"+el).autocomplete({
        source: function(request, response) {
        $.ajax({
            url: '/autocomplete/',
            dataType: "json",
            data: {
                term : request.term,
                arg  : arg,
                argb : argb
            },
             success: function (data){
                    response(data);
            }
        });
      },
    });
}
  