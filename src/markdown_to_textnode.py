from textnode import TextNode, TextType, text_node_to_html_node
def split_nodes_delimiter(old_nodes, delimiter, text_type):
    if not isinstance(old_nodes, list):
        old_nodes = [old_nodes]
    result= []
    for old_node in old_nodes:
        # If the node isn't a text type, just add it unchanged
        if old_node.text_type != TextType.NormalText:
            result.append(old_node)
            continue  # Skip to next node
        
        # If there are no delimiters, add the whole node unchanged
        if delimiter not in old_node.text:
            result.append(old_node)
            continue  # Skip to next node

        remaining_text = old_node.text

        
        while True:
        
            start_index = remaining_text.find(delimiter)
            
            if start_index == -1:
                if remaining_text:  # Only add if not empty
                    result.append(TextNode(remaining_text, TextType.NormalText))
                break


            end_index = remaining_text.find(delimiter, start_index+len(delimiter))

            if end_index == -1:
                raise Exception("cannot find closing delimiter")
            
            if start_index > 0:
                result.append(TextNode(remaining_text[:start_index], TextType.NormalText))
            
            result.append(TextNode(
                remaining_text[start_index+len(delimiter):end_index], text_type
                ))
            

            remaining_text = remaining_text[end_index + len(delimiter):]
    return result

            