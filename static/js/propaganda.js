$(document).ready(function(event){
  $(document).on('click','#center-button',function(event){
    event.preventDefault();
    var pk = $(this).attr('value');
    $.ajax({
      type: "POST",
      url: "{% url 'posts:center_section'  %}",
      data: {id: pk, 'csrfmiddlewaretoken': '{{ csrf_token }}' },
      dataType: 'json',
      success: function(response){
        $('#center-section').html(response['form'])
        console.log($('#center-section').html(response['form']));
      },
      error: function(rs,e){
        console.log(rs.responseText);

      },

    });
  });
});