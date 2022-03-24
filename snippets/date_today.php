function wpb_date_today($atts,$content = null){
extract(shortcode_atts(array('format' => ''), $atts ));
if($atts['format'] == ''){
$date_time .= date(get_option('date_format'));
} else {
$date_time .= date($atts['format']);
}
return $date_time;
}
add_shortcode('date_today','wpb_date_today');