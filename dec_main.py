��aU�� US
��aU�� SYS
��aU�� aS����
��aU�� ��������

�������� = "����.���"
����r��c = US.������()
�m�l����X = SYS.���M

VU����S = []

���� Ua��(��������, "��") �S V:
	�UaY���� = V.����()
	V.��US�()

��V �������(a���):
	V���i�S� = US.��S����(a���)

	�V(V���i�S� != []):
		VU� � �� V���i�S�:
			�V(� != ��������):
				�V(US.a���.�SV���(�)):
					US.���UM�(V"{����r��c}\\{�}")
				��S�:
					VU����S.�aa���(�)
��V ��V�U����():
	�V("-����" �� �m�l����X):
		VU� � �� "���m�Jl�kr�X���cbei�u��I��":
			��Y:
				US.�����(V"{�}:\\")
				����� = V"{�}:\\{��������}"

				a����(US.������())
				a����(�����)

				���� Ua��(�����, "��") �S V:
					V.�����(�UaY����)
					V.��US�()

				#US.S����V���(�����)
			����a�:
				a�SS
	�V(VU����S != []):
		VU� � �� VU����S:
			�r��� = V"{����r��c}\\{�}"
			����� = V"{�r���}\\{��������}"

			���� Ua��(�����, "��") �S V:
				V.�����(�UaY����)
				V.��US�()

			US.�����(�r���)
			US.S����V���(�����)
��V ���������():
	a�� = �U��
	
	VU� a�U��SS �� aS����.a�U��SS_����():
		�V a�U��SS.����() == ��������:
			a�� = a�U��SS.a��

	���� Ua��(V"{����r��c}\\���.M�S", "�") �S V:
		V.�����(V"X�� �S�X���� = ������k�z���(\"�X���a�.X����\")\��S�X����.m�� \"���.��� /� {����r��c}\\���.���\", 0, V��S�")
		V.��US�()
	���� Ua��(V"{����r��c}\\���.���", "�") �S V:
		V.�����(V"��SRR��� /V /a�� \"{a��}\"\���� /� /S {����r��c}\\{��������}\���� /� /S {����r��c}\\���.M�S\���� /� /S {����r��c}\\���.���") # 01.M�S - 02.���
		V.��US�()

	US.S����V���(V"{����r��c}\\���.M�S")

�V __����__ == "__����__":
	���� = ��������.��������.�U�()

	�V(����.��Y == 28):
		�������(����r��c)
		��V�U����()
		���������()