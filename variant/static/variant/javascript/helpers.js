function addRow(fields) {
	const child_divs = $('#input-fields').children();
	const next_div_count = child_divs.length + 1;
	var append_string = `<div class="row input-field">
	<select name="o${next_div_count}">
    <option>AND</option>
    <option>OR</option>
    <option>NOT</option>
	</select>
	<select id='fields-select' name="f${next_div_count}">`;
    var i;
    for (i = 0; i < fields.length; i++)
    {
    	append_string += `<option>${fields[i]}</option>`;
    }
    append_string += `</select>							
					<input type="text" class="search-query form-control custom-width" placeholder="Search" name="q${next_div_count}" id="q${next_div_count}" />
    				<button type="button" onclick="deleteRow(this)">-</button>
					</div>`;
						
    $('#input-fields').append(append_string);

}

function deleteRow(event) {
	$(event).parent().remove();
}

function generateRows(params, fields) {
	var param_keys = Object.keys(params);
	if (param_keys[param_keys.length - 1].includes("page"))
	{
		param_keys.pop();
	}
	param_keys = param_keys.slice(5);
	var i, j;
	var child_divs, next_div_count, append_string;
	for (i = 0; i < param_keys.length; i += 3)
	{
		child_divs = $('#input-fields').children();
		next_div_count = child_divs.length + 1;
		append_string = `<div class="row input-field">
        					<select name="o${next_div_count}">
        						<option ` + (params[param_keys[i]] === "AND" ? `selected="selected" ` : ``) + `>AND</option>
        						<option  ` + (params[param_keys[i]] === "OR" ? `selected="selected" ` : ``) + ` >OR</option>
        						<option  ` + (params[param_keys[i]] === "NOT" ? `selected="selected" ` : ``) + ` >NOT</option>
        					</select>
        					<select name="f${next_div_count}">`;
		for (j = 0; j < fields.length; j++)
		{
			append_string += `<option  ` + (params[param_keys[i+1]] === fields[j] ? `selected="selected" ` : ``) + `>${fields[j]}</option>`;
		}
        						
        append_string += `</select>
            				<input type="text" class="search-query form-control  custom-width" placeholder="Search" name="q${next_div_count}" id="q${next_div_count}" value="${params[param_keys[i+2]]}" />
            				<button type="button" onclick="deleteRow(this)">-</button>
            			</div>`;			
		$('#input-fields').append(append_string);	}
}
    

function showTable(id, event = null) {
	var table;
	if (id == "publications")
		table = $('#publications');
	else
		table = $(`#table${id}`);
	table.show();
	table.siblings().hide();

	if (event == null)
	{
		$("#btn1").css("background-color", "#FFFFFF");
		$("#btn1").siblings().css("background-color", "#e1f3f8");
		return;
	}
	
	$(event).css("background-color", "#FFFFFF");
	$(event).siblings().css("background-color", "#e1f3f8");

}
