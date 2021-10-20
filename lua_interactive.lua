scripts = {}
loaded_scripts = {}
do
    local f = io.popen("cd gamedata\\scripts && dir /b", "r")
    local files = f:read("*a")
    f:close()
    for name in files:gmatch("(%C*).script") do
        scripts[name] = true
    end
end

function load_script(name)
    _G[name] = {}
    setmetatable(_G[name], {__index = function (self, key)
        if _G[key] then return _G[key] end
        if scripts[key] then load_script(key) end
        return _G[key]
    end
})
    local f = assert(loadfile("gamedata\\scripts\\"..name..".script"))
    setfenv(f, _G[name])
    f()
    loaded_scripts[name] = true
end

do
    for name in pairs(scripts) do
        if not loaded_scripts[name] then
            load_script(name)
        end
    end
end

-------------------------------------
printf = print
ui_mcm = {
    get = function (key)
        return key == "igi_tasks/Options/debug"
    end
}

function size_table(t)
	local n = 0
	for k,v in pairs(t) do
		n = n + 1
	end
	return n
end

function copy_table(dest, src)
	for k,v in pairs(src) do
		if type(v) == "table" then
			--' ����������� ����� ���� �� ��� ���������
			dest[k] = {}
			copy_table(dest[k], v)
		else
			dest[k] = v
		end
	end
end

function dup_table(src)
	local t = {}
	copy_table(t, src)
	return t
end

utils_data = {}
utils_data.print_table = function (node, header, format_only)
	-- to make output beautiful
	local function tab(amt)
		local str = ""
		for i=1,amt do
			str = str .. "\t"
		end
		return str
	end

	local cache, stack = {},{}
	local depth = 1
	local output_str = header and ("-- " .. tostring(header) .. "\n{\n") or "{\n"
	local output = {}
	local size_t = 0
	local size_stack = 0 
	while true do
		local size = size_table(node)
		local cur_index = 1
		for k,v in pairs(node) do
			if (cache[node] == nil) or (cur_index >= cache[node]) then
				if (string.find(output_str,"}",output_str:len())) then
					output_str = output_str .. ",\n"
				elseif not (string.find(output_str,"\n",output_str:len())) then
					output_str = output_str .. "\n"
				end

				size_t = size_t + 1
				output[size_t] = output_str
				output_str = ""

				local key
				if (type(k) == "number" or type(k) == "boolean") then
					key = "["..tostring(k).."]"
				else
					key = "['"..tostring(k).."']"
				end

				if (type(v) == "number" or type(v) == "boolean") then
					output_str = output_str .. tab(depth) .. key .. " = "..tostring(v)
				elseif (type(v) == "table") then
					output_str = output_str .. tab(depth) .. key .. " = {\n"
					size_stack = size_stack + 1
					stack[size_stack] = node
					size_stack = size_stack + 1
					stack[size_stack] = v
					cache[node] = cur_index+1
					break
				elseif (type(v) == "userdata") then
					if (v.diffSec) then
						local Y, M, D, h, m, s, ms = 0,0,0,0,0,0,0
						Y, M, D, h, m, s, ms = v:get(Y, M, D, h, m, s, ms)
						output_str = string.format("%s%s%s = { Y=%s, M=%s, D=%s, h=%s, m=%s, s=%s, ms=%s } ",output_str,tab(depth),key,Y, M, D, h, m, s, ms)
					else
						output_str = output_str .. tab(depth) .. key .. " = userdata"
					end
				else
					output_str = output_str .. tab(depth) .. key .. " = '"..tostring(v).."'"
				end

				if (cur_index == size) then
					output_str = output_str .. "\n" .. tab(depth-1) .. "}"
				else
					output_str = output_str .. ","
				end
			else
				-- close the table
				if (cur_index == size) then
					output_str = output_str .. "\n" .. tab(depth-1) .. "}"
				end
			end

			cur_index = cur_index + 1
		end
		
		if (size == 0) then
			output_str = output_str .. "\n" .. tab(depth-1) .. "}"
		end

		if (size_stack > 0) then
			node = stack[size_stack]
			stack[size_stack] = nil
			size_stack = size_stack - 1
			depth = cache[node] == nil and depth + 1 or depth - 1
		else
			break
		end
	end
   
	size_t = size_t + 1
	output[size_t] = output_str

	output_str = table.concat(output)
	
	printf(output_str)
end

print_table = utils_data.print_table
