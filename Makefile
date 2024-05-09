# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Makefile                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: dherszen <dherszen@student.42.rio>         +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/03/31 18:19:08 by dherszen          #+#    #+#              #
#    Updated: 2024/03/31 18:30:05 by dherszen         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

checkpoint:
			@git add -A
			@git commit -m "checkpoint at $$(date '+%Y-%m-%dT%H:%M:%S%z')"
			@git push
			@echo Checkpoint created and pushed to remote

PHONY: checkpoint
